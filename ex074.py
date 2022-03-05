"""Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint

numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),)
menor = None
maior = None

for numero in numeros:
    if menor is None:
        menor = numero
    else:
        if numero < menor:
            menor = numero
    if maior is None:
        maior = numero
    else:
        if numero > maior:
            maior = numero

print(numeros)
print(f'O maior número é:{maior}')
print(f'O menor número é:{menor}')

###########################################################OUTRA FORMA##################################################


for n in numeros:
    print(f'{n} ',end = '')
# a funçao max e min recebe como parametro uma tupla
print(f'\nO maior número é:{max(numeros)}')
print(f'O menor núnmero é:{min(numeros)}')