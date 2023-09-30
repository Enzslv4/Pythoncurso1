"""
try/except
try -> tenta executar o codigo
except -> ocorreu algum erro ao tentar execultar
"""
numero = input('Digite um número: ')

try:
    print('STR: ', numero)
    numfloat = float(numero)
    print('FLOAT: ', numfloat)
    print(f'O dobro de {numero} é {numfloat * 2:.1f}')
except:
    print('Isso não é um número')