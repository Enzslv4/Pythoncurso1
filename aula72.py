# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos

# Retorne o total para uma variável e mostre o valor
# da variável.

#def mult(*args):
    #total = 1
    #for numeros in args:
        #total *= numeros
    #return total

#my_numbs = (mult(1,2,3,4,5,6))
#print(my_numbs)
import os
while True:
    try:
        os.system('cls')
        print('Par ou impar')
        numero = int(input('Digite o numero: '))
        par = (numero % 2 == 0)
        def par_ou_impar(*args):
            if par:
                return f'{numero} é par'
            return f'{numero} é ímpar'
        
        print(par_ou_impar(numero))
    except:
        print('Voce precisa digitar dois numeros!')
    sair = input('Quer [s]air? ').lower().startswith('s')
    if sair:
        break