"""
Iterável - str, range, etc (__iter__)
'__' chamado de thunder
utiliza método
Iterador - quem sabe entregar um valor por vez
next - me entregue o prox valor
iter - me entregue seu iterador
"""

texto = input('Digite seu nome: ') # iteravel
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break