"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres de str
"""

vari = 'Olá Mundo'
print(vari[7])

#fatiamento
print(vari[4:])

#contar caracteres com len
print(len(vari))

#passo - p(pula caracteres)
print(vari[0:9:2])
print(vari[::-1])
print(vari[::-2])