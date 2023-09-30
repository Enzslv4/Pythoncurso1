# formatação de strings = f

nome = 'Enzo Silva Leal'
altura = 1.8
peso = 65
imc = peso / (altura ** 2)

linha1 = f'{nome} tem {altura:.2f} de altura,'
# .2f = para saber quantas casas decimais vc quer q aparareça
# dps da vírgula, o 2 pode ser outro numero, nesse caso
# indica 2 casas decimais
# para separar os milhares, basta colocar ',.xf' para isso
linha2 = f'pesa {peso} quilos e seu IMC é'

print(linha1)
print('pesa', peso, 'quilos e seu IMC é')
print(f'{imc:.2f}')