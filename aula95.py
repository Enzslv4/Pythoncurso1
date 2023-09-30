# raise - lançamentos de exeçoes
# para relançar um erro, basta escrever somente o raise

def nao_pode_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não pode dividir por 0')
    return True

def nao_pode_str(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float.', 
            f'"{tipo_n.__name__}" enviado.')
    return True

def divide(n, d):
    nao_pode_zero(d)
    nao_pode_str(n)
    nao_pode_str(d)
    try:
        return n/d
    except ZeroDivisionError:
        return n

print(divide(18,'2'))