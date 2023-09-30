# desempacotamento em chamadas
# de metodos e funções

string = 'ABCD'
lista = ['Maria', 'Joao', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

#p, b, *_, ap, u = lista
#print(p, u, ap)

'''
Outra forma de desempacotar:
for nome in lista:
    print(nome, end=' ')
    o end serve para ele desempacotar tudo 
    em uma só linha
'''

print(*lista) # forma mais simples