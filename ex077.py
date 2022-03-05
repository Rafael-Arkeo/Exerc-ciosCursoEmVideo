"""Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras =('Casa','Boneca','voassoura','cavalo','chuveiro','fruta')
vogais = ('a','e','i','o','u')

for pos in range(0, len(palavras)):
    print(f'{palavras[pos]:.<30}vogais:', end='')

    for letra in palavras[pos]:
        if letra in vogais:
            print(f'{letra}\n',end='')
