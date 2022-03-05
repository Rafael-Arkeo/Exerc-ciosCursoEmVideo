"""Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Italiano de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Sassuolo."""


classificacao = ('Inter', 'Napoli', 'Milan', 'Juventus', 'Atalanta', 'Lazio', 'Roma',
                 'Fiorentina', 'Verona', 'Torino', 'Empoli', 'Sassuolo', 'Bologna', 'Udinese', 'Spezia',
                 'Sampdoria', 'Cagliari', 'Venezia', 'Genoa', 'Salernitania')


print('\t\t\t\tSeria A Tim')
print('-='*30)

print('Os primeiros 5 colocados são:')
for pos, time in enumerate(classificacao[0:5]):
    print(f'{pos +1}:{time}')
print('-='*30)

print('Os 4 ultimos colocados são:')
c = 19
pos2 = 20
for time2 in classificacao[19:15:-1]:
    print(f'{pos2}:{time2}')
    pos2 -= 1

print('-='*30)

print('Os times em ordem alfabética:')
for time3 in sorted(classificacao):
    print(time3)
print('-='*30)

print(f'O {classificacao[11]} ocupa a {classificacao.index("Sassuolo") + 1}° posição')