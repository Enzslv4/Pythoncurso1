'''
args - argumentos nao nomeados
serve pra colocar a quantidade de argumentos que vc quiser,
msm q ainda não estejam definidos
* - *args (empacotamento e desempacotamento)
'''

def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total += numero
        print('Total', total)

numeros = 1, 2, 3, 4, 5, 6, 7, 8 # isso é uma tupla
outra_soma = soma(*numeros)
print(outra_soma) # é preciso primeiro desempacotar a tupla para poder executar a soma,
# pois a tupla se comporta como uma só iteravel
soma(1,2,3,4,5,6,7,8)

print(sum((numeros)))