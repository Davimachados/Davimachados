from random import randint
from time import sleep
velcarro = randint(1, 90)
print('=' * 70)
print('VRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUM')
print('EI! Você viu isso? Certamente era o Francesco Virgolini... Mas, a que velocidade ele estava? Vamos ver se ele')
print('foi multado pelo nosso radar.')
print('PROCESSANDO')
sleep(2)
if velcarro <= 80:
    print('Parece que ele estava apenas a {} KM/h, ele realmente parecia mais rapido, mas desta vez escapou!'.format(velcarro))
else:
    print('ORA ORA, PARECE QUE O FRANCESCO ESTAVA A {}KM/h, DESSA VEZ ELE NÃO ESCAPA, CALCULE A MULTA, POR FAVOR!'.format(velcarro))
    multa = velcarro * 7
    sleep(3)
    print('Certo, a multa de R${:.2f} será mandada para a casa dele.'.format(multa))
print('Bom, ainda temos mais 2 horas de expediente, vamos nos manter atentos!')