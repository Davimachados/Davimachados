n1 = int(input('Por favor, digite um valor inteiro: '))
print('Por favor, selecione uma de nossas opções de conversão:')
print('[1] = Binário ')
print('[2] = Octal ')
print('[3] = Hexadecimal')
print('[0] = Sair do conversor')
conv = str(input('Qual conversão deseja? '))
if conv == '1':
    binar = str(bin(n1))
    print('O valor {} em binário é: {}'.format(n1, binar))
elif conv == '2':
    octal = str(oct(n1))
    print('O valor {} em octal é: {}'.format(n1, octal))
elif conv == '3':
    hexad = str(hex(n1))
    print('O valor {} em Hexadecimal é: {}'.format(n1, hexad))
elif conv == '0':
    print('Encerrando programa.')