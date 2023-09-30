"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

# Definição
def soma(x, y):
    print(f'{x=} e {y=}', '/', 'x + y =', x + y)

soma(1, 2)
soma(y=2, x=1) # para definir a ordem em que as variaveis sao definidas