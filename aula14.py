#formatação com o "format"

a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )
# ao adicionar valores entre os parenteses,
# vc consegue escolher a ordem em q as coisas aparecem
# da para criar um parametro q se refere ao objeto
# como o 'nome1', que é um parametro q se refere
# ao objeto 'a'
print(formato)