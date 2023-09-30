"""
while/else

nesse caso é possivel usar o else como uma forma de
continuar o laço mesmo q antes tenha um break
"""

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Nao encontrei espaços')

print('Fim do laço')