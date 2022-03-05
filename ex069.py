"""Crie um programa que leia a idade eo sexo de várias pessoas.
   A cada pessoa cadastrada,o programa deverá perguntar se a pessoa quer ou nõa continuar.
   No final mostre:

   A) Quantas pessoas tem mais de 18 anos.

   B) Quantos homens foram cadastrados.

   C) Quantas mulheres tem menos de 20 anos."""

from time import sleep

print('-=' *5, 'ANÁLISE DE DADOS', '-=' *5)


pessoa_maior = 0
masculino = 0
mulher_menor_20 =0

condicao = 0
while condicao == 0:
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        pessoa_maior +=1
    sexo = str(input('Digite o sexo da pessoa masculino ou feminino[M/F]: ')).strip().upper()
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1

    while True:
        continuar = str(input('Você deseja continuar[S/N]: ')).strip().upper()
        if continuar == 'N':
            condicao +=1
            break
        elif continuar == 'S':
            condicao = condicao
            break
        else:
            print('Digite um opção válida!')




print('Analisando os dados.......')
sleep(3)
print('Pronto')
print(f'{pessoa_maior} pessoas tem mais de 18 anos')
print('-=' * 20)
print(f'{masculino} homens foram cadastrados')
print('-=' *20)
print(f'{mulher_menor_20} mulheres com menos de 20 anos foram cadastradas')
print('-=' *20)
print('FIM')
print('-=' *20)

print(' ')
print(' ')

while True:
    next = str(input('Quer ver a  versão do professor[s/n: ')).strip().upper()
    if next == 'N':
        break
    else:

        print('-=' * 5, 'ANÁLISE DE DADOS 2', '-=' * 5)

        tot18 =0
        totm = 0
        totM20 = 0
        while True:
            print('Informe o sexo ea idade da pessoa')
            idade2 = int(input('Idade: '))
            sexo2 = ' '
            while sexo2 not in 'MF':
                sexo2 = str(input('Sexo: [M/F]: ')).strip().upper()
                if sexo2 != 'M' and sexo2 != 'F':
                    print('Digite [M] para MASCULINO ou [F] para FEMENINO!')
            if idade2 >= 18:
                tot18 += 1
            if sexo == 'M':
                totm += 1
            if idade2 < 20 and sexo == 'F':
                totM20 += 1

            resp = ' '
            while resp not in 'SN':
                resp = str(input('Quer continuar [S/n]:')).strip().upper()

                if resp == 'N':
                    break
        print('Analisando os dados.......')
        sleep(3)
        print(f'Total de pessoas com mais de 18 anos: {tot18}')
        print('-=' * 20)
        print(f'Ao todo temos {totm} homens cadastrados')
        print('-=' * 20)
        print(f'E temos {totM20} mulheres com menos de 20 anos')
        print('-=' * 20)





print('FIM')# Solução do professor