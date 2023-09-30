"""
interpolações basicas de strings
's' - string
'd' e 'e' - int
f - float
'x' e 'X' - Hexadecimal(minusculo e maiusculo)
"""

nome = 'Enzo'
preco = 1000.9484366
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

# para transformar da base 10 para a hexadecimal:
# %x
print('O hexadecimal de %d é %x' % (15, 15))
# para preencher casas: %04x ou %04X
print('O hexadecimal de %d é %04x' % (1500, 1500))