print('-='*15)
print(f'\t\tBANCO CV')
print('-=' *15)


saque = int(input('Que valor você quer sacar?:'))
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula01 = 0
while saque > 0:
    while saque >= 50:
        saque -= 50
        cedula50 += 1
    while saque >= 20:
        saque -= 20
        cedula20 += 1
    while saque >= 10:
        saque -= 10
        cedula10 += 1
    while saque >= 1:
        saque -= 1
        cedula01 += 1
if cedula50 > 0:
    print(f'{cedula50} cedulas de R$50')
if cedula20 > 0:
    print(f'{cedula20} cedulas de R$20')
if cedula10 > 0:
    print(f'{cedula10} cedulas de R$10')
if cedula01 > 0:
    print(f'{cedula01} cedulas de R$1')

########################## solução do professor #################################################

print('Fim\n\n')

print('-='*15)
print(f'\t\tBANCO CV')
print('-=' *15)

retirada = int(input('Qual valor vc quer retirar:R$'))
total = retirada
ced = 50
totalced =0

while True:
    if total >= ced:
        totalced -= ced
        totalced += 1
