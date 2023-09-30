'''
Imprecisão - round()
'''

import decimal

num_a = decimal.Decimal(0.1) # da mais precisão ao numero equacionado
num_b = decimal.Decimal(0.7)
num_c = num_a + num_b
num1 = 0.1
num2 = 0.7
num3 = num1 + num2
print(num3) # double precision float-point format
print(f'{num3:.2f}')
print(round(num3, 2)) # 'resolve' esse problema
print(num_c)