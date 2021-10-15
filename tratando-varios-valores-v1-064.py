"""Exercício Python 64:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)."""


#criar uma lista para armazenar os valores
#chamar a função para o usuário digitar os valores e armazenar na lista
#criar funçao que retorne os valore na ordem em que foram digitados
#mostrar soma desses valores


soma_num = 0
conta_num = 0
num = 0


while num != 999:
    num = int(input('Digite um número inteiro ou [999] para encerrar o programa:'))
    if num != 999:
        soma_num += num
        conta_num += 1
print(f'Você digitou {conta_num} e a soma entre eles é {soma_num}!')