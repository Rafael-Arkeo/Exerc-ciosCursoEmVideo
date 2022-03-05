"""Exercício Python 72:
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

num_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                   'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                   'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 0 e 20 ou -1 para encerrar o programa:'))
    if num >=0 and num <= 20:
        print(f'Vc digitou:{num_por_extenso[num]}')
    elif num == -1:
        break
    else:
        print('Digite uma opção válida!')

print('FIM')
