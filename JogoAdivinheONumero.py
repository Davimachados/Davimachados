from random import randint
computador = randint(0, 5) #Faz o computador pensar em um numero aleatorio
print('#' * 20)
print('Vou pensar em um numero de 0 a 5, adivinhe se for capaz, frango.')
print('#' * 20)
jogador = int(input('Em que numero eu pensei?')) #Usuario tenta adivinhar
print('ANALISANDO RESPOSTA')
if jogador == computador:
    print('É, parece que você me venceu desta vez, és um jogador formidável!')
    print('Espero que possamos jogar novamente algum dia, até mais, plebeu.')
else:
    print('HAHAHAHA VOCÊ PENSOU MESMO QUE O CEREBRO HUMANO PODERIA ME PREVER? EU? UMA MÁQUINA? HAHAHAHAH')
    print('Foi divertido humilhar você, se algum dia quiser tentar novamente, basta me desafiar novamente, espécie inferior.')