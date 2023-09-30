"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '246.610.390-76'
#cpf = input('Digite o cpf: ')

cpf_inicio = cpf.split('.')
unida1 = '-'.join(cpf_inicio)
cpf_num = unida1.split('-')

i = 0
cpf_total = ''
while i <= 2:
    cpf_part = ''.join(cpf_num[i])
    cpf_total += cpf_part.strip()
    i += 1

multiplicador = 10
produto = 0
soma = 0
for num in cpf_total:
    produto = int(num) * multiplicador
    soma += produto
    multiplicador -= 1

divisor = (soma * 10) % 11

if divisor > 9:
    divisor = 0

#cpf_num[3]

num1 = list(cpf_num[3])

if divisor == int(num1[0]):
    print('Seu CPF é válido.')
else:
    print('Seu CPF não é válido.')