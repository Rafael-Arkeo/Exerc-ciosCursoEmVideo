"""Exercício Python 70:
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato"""

print('-=' *5, 'ESTATÍSTICAS DE PRODUTOS', '-=' *5)

total_gastos = 0
preco_maior_1000 = 0
produto_mais_barat0 = str
menor_preco = -1


while True:
    nome = str(input('Digite o nome do produto:')).lower()
    preco = float(input('Digite o preço do produto:'))
    if menor_preco < 0:
        total_gastos += preco
        produto_mais_barat0 = nome
        if preco > 1000:
            preco_maior_1000 += 1
    if menor_preco >= 0:
        total_gastos += preco
        if preco > 1000:
            preco_maior_1000 += 1
        if preco < menor_preco:
            menor_preco = preco
            produto_mais_barat0 = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar= str(input('Continuar:[S/N]:')).strip().upper()
    if continuar == 'N':
        break



print(f'O preço total gasto foi: {total_gastos}')
print(f'{preco_maior_1000} produtos custam mais de R$1000,00')
print(f'{produto_mais_barat0} é o produto mais barato')