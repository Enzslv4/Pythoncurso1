'''
Retorno das funções - retorna valores (return)
só pode existir um return por função, e esse return so pode retornar um valor,
depois disso ele termina o codigo
'''

def soma(x, y):
    if x > 10:
        return 10
    return x + y

soma1 = soma(1, 2)
soma2 = soma(2, 5)
print(soma1 + soma2)