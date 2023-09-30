"""
iterando string com while
"""

nome = input('Digite seu nome: ')
tam = len(nome)
lugar = 0
novo = ''

while lugar < tam:
    novo += f'{nome[lugar]}*'
    lugar += 1
    

print(f'*{novo}')