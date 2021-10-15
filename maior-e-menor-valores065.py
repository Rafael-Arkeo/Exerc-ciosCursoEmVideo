"""Exercício Python 65:
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""


#crie quatro variáveis para armazenar o valor digitado pelo usário,o maior,o menor ea média
#crie uma variável para o teste lógico


maior = menor = soma = cont = media = 0

resp = 'S'


while resp in 'Ss':
    num = int(input('Digite um número:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    resp = str(input('Quer continuar? [s/n]:')).upper().strip()[0]
media = soma / cont
print(f'A média entre todos os números é {media}!')
print(f'O maior entre eles foi o número {maior}!')
print(f'O menor entre eles foi o número {menor}!')




