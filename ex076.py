"""Exercício Python 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

pyshop = ('Camisa Gola Polo', 78.90,
          'Calça Jeans', 124.75,
          'Sapato Bico Fino', 245.00,
          'Bone Aba Reta', 87.50)


print('-='*30 )
print(f'{"PyShop":^40}')
print('-='*30 )

print(f'{"Tabela de preços":^40}')
for pos in range(0, len(pyshop)):
    if pos % 2 == 0:
        print(f'{pyshop[pos]:.<30}', end='')
    else:
        print(f'R${pyshop[pos]:.>7}')