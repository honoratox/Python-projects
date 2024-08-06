import pygame #biblioteca de criação de jogos
import os #biblioteca que permite integrar o código com os arquivos do pc, ex: a oasta de imgs
import random #biblioteca de geração de números aleatórios

#definição de constantes (valores imutáveis)
TELA_LARGURA = 500
ALTURA_TELA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird&AI', 'imgs', 'pipe.png'))) #transforma(transform) a escala da imagem (scale) que vamos usar, depende da quantidadee (2x)
                                                                                            #usa a biblioteca (pygame), com quem quer fazer, no caso a imagem (image) e a ação, que é carregar (load), e passa o caminho ('')
                                                                                            #usa a biblioteca (os) pra acessar os arquivos do pc (pasta imgs) e o arquivo que voce quer                                          
IMAGEM_CHAO =  pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird&AI', 'imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird&AI', 'imgs', 'bg.png')))
IMAGENS_PASSAR0 = [ #como são mais de 1 imagem de pássaro, se cria uma lista ([]), pra poder passar todas
    pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird&AI', 'imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird&AI', 'imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird&AI', 'imgs', 'bird3.png')))
]

pygame.font.init() #inicializa a fonte
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


#criação de objetos de movimento

class Passaro:
    IMGS = IMAGENS_PASSAR0 # busca a constante através de uma variável

    #animações da rotação do pássaro / sem a rotação a troca de imagens do pássaro fica muito dura, isso serve pra deixar mais fluido
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    #atributos do pássaro (posição eixo x e y, altura, velocidade e etc)
    def __init__(self, x, y): #DEFINIR AS POSIÇÕES INICIAIS
        self.x = x #posição inicial
        self.y = y #posição inicial
        self.angulo = 0 
        self.velocidade = 0 #velocidade de movimentação pra cima e pra baixo
        self.altura = self.y #altura é sua posição no eixo y
        self.tempo = 0 #o tempo de animação das imagens
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0] #seleciona a primeira imagem


    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y


    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo #basicamente informa a fórmula do deslocamente 1.5 x tempo^2 + velocidade x tempo


        #resringir o deslocamento pro pássaro nao acelerar infinitamente
        if deslocamento > 16:
            deslocamento = 16 #defini 16 como deslocamento máximo
        elif deslocamento < 0:
            deslocamento -= 2 #aumenta o tanto que o passaro pula, or padrão pula pouco

        self.y += deslocamento #efetivamente fazer o deslocamento, soma 'deslocamento' ao eixo 'y'


        #angulo do pássaro -> só controla o angulo de rotação
        if deslocamento < 0 or self.y < (self.altura +50): #se o passaro se manter acima da sua posição inicial
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO


    def desenhar(self, tela):
        #definir qual imagem do passaro vai usar
        self.contagem_imagem += 1 #quando a contagem de imagem bater 5, muda, bateu10, muda de novo e por ai vai
        
        if self.contagem_imagem < self.TEMPO_ANIMACAO: #significa que eu ainda to na primeira imagem
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2: #significa que eu ainda to na segunda imagem
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3: #significa que eu ainda to na terceira imagem
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4: #precia fazer o movimento dde asa completo, dessa vez subindo
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1: #se for maior que o cara anterior, recomeça o ciclo
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0 #zera a contagem de imagem pra poder recomeçar o ciclo


        #se o passaro tiver caindo, não vou bater asa
        if self.angulo <= 80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2 #só por estética, definie que quando quaindo a batida de asa vai ser pra baixo, como se tivesse se impulsionando


        #desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo) #rotacionando a imagem e quantos graus (angulo)
        posicao_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=posicao_centro_imagem) #é como se pegasse a imagem e desenhasse um retangulo ao redor dela
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self): #função pra pegar a máscara do pássaro, basicamente divide aquele retangulo que representa todas as imagens adicionadas, em pixels, depois verifica se dentro desse pixel tem tanto o objeto passaro quanto o objeto cano, pra validar se teve ou não colisão
        return pygame.mask.from_surface(self.imagem) #pega a máscara do pássaro


class Cano:
    DISTANCIA = 200 #distancia de um cano pro outro, pro passaro poder passar
    VELOCIDADE = 5 #velocidade que os canos vão se movimentar pra esquerda

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.posicao_topo = 0 #posição do cano de cima no eixo y
        self.posicao_base = 0 #posição do cano de baixo no eixo y
        self.IMG_CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True) #flip da imagem do cano
        self.IMG_CANO_BASE = IMAGEM_CANO
        self.passou = False #verificar se o pássaro ja passou do cano ou nao
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450) #a altura total da tela é 800, podia só deixar o random, porém, para não ficar uma passagem extremamente longe da outra, defini um range pra isso (randrange)
        self.posicao_topo = self.altura - self.IMG_CANO_TOPO.get_height()
        self.posicao_base = self.altura + self.DISTANCIA 


    def mover_cano(self):
        self.x -= self.VELOCIDADE #mover o cano pra esquerda


    def desenhar_cano(self, tela):
        tela.blit(self.IMG_CANO_TOPO, (self.x, self.posicao_topo))
        tela.blit(self.IMG_CANO_BASE, (self.x, self.posicao_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.IMG_CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.IMG_CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.posicao_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.posicao_base - round(passaro.y))

        topo_ponto_colisao = passaro_mask.overlap(topo_mask, distancia_topo) #'overlap' - verifica se tem 2 pixels iguais, no caso do passaro pra base
        base_ponto_colisao = passaro_mask.overlap(base_mask, distancia_base) #'overlap' - verifica se tem 2 pixels iguais, no caso do passaro pra base

        if base_ponto_colisao or topo_ponto_colisao: #se existir colisão returna true, caso contrário false
            return True
        else:
            return False


class Chao:
    VELOCIDADE = 5 #se movimenta na mesma velocidade que o cano
    LARGURA = IMAGEM_CHAO.get_width() #pega a largura da imagem do chão
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.chao1 = 0
        self.chao2 = self.LARGURA

    def mover_chao(self):
        self.chao1 -= self.VELOCIDADE 
        self.chao2 -= self.VELOCIDADE

        if self.chao1 + self.LARGURA < 0: #verifica se o chao1 saiu todo da tela
            self.chao1 = self.chao2 + self.LARGURA #envia o chao 1 pra tras do chao 2
        if self.chao2 + self.LARGURA < 0:
            self.chao2 = self.chao1 + self.LARGURA


    def desenhar_chao(self, tela): #desenha o chão
        tela.blit(self.IMAGEM, (self.chao1, self.y))
        tela.blit(self.IMAGEM, (self.chao2, self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0,0)) #desenhar o fundo da tela imovel e no centro
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar_cano(tela)

    # Desenhar o fundo para a pontuação
    fonte_game_over = pygame.font.SysFont('arial', 30) #fonte e tamanho do texto de pontuação
    texto_pontuacao = fonte_game_over.render(f"Pontuação: {pontos}", True, (255, 255, 255)) #o 'f' antes da string informa que uma variável vai ser passada dentro da própria string, no caso, pontos
                                                                                            #'render' imprime o texto dentro da tela
                                                                                            #os números dentro dos () são os dados das cores no padrão rgb
    largura_texto = texto_pontuacao.get_width()
    altura_texto = texto_pontuacao.get_height()

    # Desenhar retângulo preto com bordas arredondadas
    rect_x = TELA_LARGURA - 20 - largura_texto - 7 #define a distância do box para a lateral
    rect_y = 10 - 5 #define o espaço entre o box e o topo da tela
    rect_largura = largura_texto + 15 #define o comprimento do box de fundo de pontuação
    rect_altura = altura_texto + 10 #define a altura do box de fundo de pontuação

    pygame.draw.rect(tela, (0, 0, 0), (rect_x, rect_y, rect_largura, rect_altura), border_radius=15)  # fundo preto com bordas arredondadas
    tela.blit(texto_pontuacao, (TELA_LARGURA - 10 - largura_texto - 10, 10))

    chao.desenhar_chao(tela)
    pygame.display.update()

def main():
    passaros = [Passaro(230, 350)]  # posição inicial do pássaro
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, ALTURA_TELA))
    pontos = 0
    relogio = pygame.time.Clock()  # pygame já tem a dinâmica da animação de tempo, para atualizar a tela

    jogo_ativo = True  # Variável para controlar se o jogo está ativo ou não
    rodando = True

    while rodando:  # o jogo é um loop infinito
        relogio.tick(30)  # atualizar 30 frames por segundo

        # interação com o usuário
        for evento in pygame.event.get():  # dispara um evento (clicar o mouse, apertar espaço e etc)
            if evento.type == pygame.QUIT:  # se apertar o X para fechar o jogo
                rodando = False
            if evento.type == pygame.KEYDOWN:  # KEYDOWN verifica se a tecla foi clicada
                if evento.key == pygame.K_SPACE:  # verifica se a tecla foi o espaço
                    if jogo_ativo:  # só permite pular se o jogo estiver ativo
                        for passaro in passaros:
                            passaro.pular()  # faz o pássaro pular

        if jogo_ativo: #se o jogo se manter ativo
            # mover as coisas
            for passaro in passaros:
                passaro.mover()
            chao.mover_chao()  # chama o método correto para mover o chão

            adicionar_cano = False
            remover_canos = []
            for cano in canos:
                for i, passaro in enumerate(passaros):  # pega a posição do pássaro dentro da lista
                    if cano.colidir(passaro):  # se o cano bateu com o pássaro
                        jogo_ativo = False  # para o jogo se houver colisão
                        break  # interrompe o loop de colisões

                    if not cano.passou and passaro.x > cano.x:  # se a variável cano.passou é falsa, mas o pássaro passou
                        cano.passou = True #converte pra True o False de passar o cano
                        adicionar_cano = True
                cano.mover_cano()
                if cano.x + cano.IMG_CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)  # adiciona os canos que saíram da tela a uma lista de exclusão

            if adicionar_cano:
                pontos += 1  # se passar do cano, ganha um ponto
                canos.append(Cano(600))  # adiciona um cano antes da tela se mover

            for cano in remover_canos:
                canos.remove(cano)  # remove todos os canos dentro da lista

            # definir colisão acima e abaixo
            for i, passaro in enumerate(passaros):
                if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:  # define a colisão com o chão e com o teto
                    jogo_ativo = False  # para o jogo se houver colisão
                    passaros.pop(i)

            desenhar_tela(tela, passaros, canos, chao, pontos)

        else:  # se houver colisão = game over
            # Tela de Game Over
            fonte_game_over = pygame.font.SysFont('arial', 60)
            texto_game_over = fonte_game_over.render('Game Over', True, (255, 255, 255))  # 'render' imprime o texto dentro da tela
                                                                                          # os números dentro dos () são os dados das cores no padrão rgb
            largura_texto = texto_game_over.get_width()
            altura_texto = texto_game_over.get_height()

            # Desenhar retângulo vermelho com bordas arredondadas
            rect_x = TELA_LARGURA // 2 - largura_texto // 2 - 10  # centraliza o retângulo na tela
            rect_y = ALTURA_TELA // 2 - altura_texto // 2 - 10  # centraliza o retângulo na tela
            rect_largura = largura_texto + 20
            rect_altura = altura_texto + 20

            pygame.draw.rect(tela, (212, 0, 0), (rect_x, rect_y, rect_largura, rect_altura), border_radius=15)  # fundo vermelho com bordas arredondadas
            tela.blit(texto_game_over, (TELA_LARGURA // 2 - largura_texto // 2, ALTURA_TELA // 2 - altura_texto // 2))

            # Tela de Reinício
            fonte_restart = pygame.font.SysFont('arial', 40)
            texto_restart = fonte_restart.render('Aperte R para reiniciar', True, (255, 255, 255))
            largura_texto2 = texto_restart.get_width()
            altura_texto2 = texto_restart.get_height()

            # Desenhar retângulo amarelo com bordas arredondadas abaixo do retângulo de Game Over
            rect_a = TELA_LARGURA // 2 - largura_texto2 // 2 - 5
            rect_b = rect_y + rect_altura + 20  # Posição logo abaixo do retângulo de Game Over
            rect_largura2 = largura_texto2 + 20
            rect_altura2 = altura_texto2 + 20

            pygame.draw.rect(tela, (253, 207, 0), (rect_a, rect_b, rect_largura2, rect_altura2), border_radius=15)
            tela.blit(texto_restart, (TELA_LARGURA // 2 - largura_texto2 // 2, rect_b + 10))

            pygame.display.update()
           
            pygame.display.update()

            # Congela a tela até que o jogador tome uma ação
            game_over = True
            while game_over:
                for evento in pygame.event.get():  # permite que o usuário feche o jogo na tela de Game Over
                    if evento.type == pygame.QUIT:
                        rodando = False
                        game_over = False
                    if evento.type == pygame.KEYDOWN:  # permite que o jogador feche o jogo ou reinicie
                        if evento.key == pygame.K_ESCAPE:  # tecla ESC para sair
                            rodando = False
                            game_over = False
                        if evento.key == pygame.K_r:  # tecla R para reiniciar
                            main()  # reinicia o jogo
                            return  # retorna para evitar execução dupla

if __name__ == '__main__':
    main()