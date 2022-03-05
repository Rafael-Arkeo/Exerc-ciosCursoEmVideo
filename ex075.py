"""Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

numeros = (int(input('Digite um número:')),
               int(input('Digite o segundo número:')),
                   int(input('Digite o tercerio número:')),
                       int(input('Digite o quarto número:'),))

print(f'Você digitou os números: {numeros}')
if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)} vezes!')
else:
    print('O número 9 não foi digitado!')
if 3 in numeros:
    print(f'O número 3 apareceu a primeira vez na {numeros.index(3)}º posição!')
else:
    print('O número 3 não foi digitado!')
print('Os números pares sáo:', end= ' ')
for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}', end= ',')