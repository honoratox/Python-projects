# Flappy Bird and A.I

## Portugês
Nesse projeto eu tive que replicar o famoso jogo Flappy Bird e usei de uma Inteligência Artificial (I.A), também criada por mim, para que a mesma aprendesse a jogar de forma autônoma utilizando aprendizagem de máquina.  

Para isso eu criei versões (v01.py, v02.py, ...) e acada versão eu dificucltava ainda mais, acrescentava mais canos, fazia eles se moverem aleatoriamente, tudo isso para a IA ser "vencida", porém inevitavelmente uma hora ela se tornou imortal no jogo.  

### Aspectos Técnicos
Para a IA eu usei o algorítimo do NEAT (Neural Evolution Augmenting Topology), basicamente é uma IA baseada em uma rede neural que evolui ao longo do tempo, usando algo similar a seleção natural de Darwin.  

Os pássaros são inicialmente gerados aleatoriamente em grupos de 100, os melhores dentre esses são clonados com pequenas modificações em grupos de 100 novamente, chamamos esses grupos de gerações, e assim vai até que exista um pássaro com os valores ideias para se tornar imortal

## English
In this project I had to replicate the famous Flappy Bird game and used an Artificial Intelligence (A.I.), also created by me, so that it could learn to play autonomously using machine learning.  

For this I created versions (v01.py, v02.py, ...) and with each version I made it even more difficult, added more pipes, made them move randomly, all this so the AI ​​could be "beaten", but inevitably eventually she became immortal in the game.