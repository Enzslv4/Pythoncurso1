'''
Listas dentro de listas
'''

salas = [
    ['Maria', 'Joao', 'Pedro', 'Paulo'],
    ['Mario', 'Erica', 'Enzo', 'Jorge'],
    ['José', 'Ana', 'Flavio', 'Irineu']
]

print(f'*{salas[1][2]}*')
i = 1
for sala in salas: # para mostrar todos os itens separadamente
    print(f'A sala é a número {i}:')
    i += 1
    for aluno in sala:
        print(aluno)