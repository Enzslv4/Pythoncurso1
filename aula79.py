# exemplo de set
letras = set()
while True:
    letra = input('Digite sua letra: ')
    letras.add(letra.lower())
    print(letras)
    if 'e' in letras:
        print(f'Parabens, "{letra}" é a letra!')
        break
