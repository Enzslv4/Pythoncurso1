# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula97_m

print('Este módulo se chama', __name__)

i = 0
recebidos = ''
numeros = []
while i < 2:
    recebidos = input('Digite um número: ')
    numeros.append(int(recebidos))
    i += 1

print(aula97_m.divide(numeros))
