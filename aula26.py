"""
Formatação básica de strings
s - strings
d - int
f - float
.<numero de digitos>f
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - ou +
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.736893:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')