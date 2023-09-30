import os

cript = 'computador'
letras_certas = ''
tentativas = 0

while True:
    letradig = input('Digite uma letra: ')
    tentativas += 1
    if len(letradig) > 1:
        print('Digite apenas uma letra.')
        continue
    if letradig in cript:
        letras_certas += letradig
    
    palavraform = ''
    for letrasec in cript:
        if letrasec in letras_certas:
            palavraform += letrasec
        else:
            palavraform += '*'
    
    print(f'Palavra formada: {palavraform}')

    if palavraform == cript:
        os.system('cls')
        print('Voce ganhou, parabéns!')
        print('O numero de tentativas foi', tentativas)
        letras_certas = ''
        tentativas = 0
