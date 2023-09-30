# exercicio 3

nome = input('Digite seu nome: ')
tamanho = len(nome)
pequeno = tamanho <= 4
medio = 5 <= tamanho <= 6

if not(' ' in nome):
    if tamanho > 1:
        if pequeno:
            print('Seu nome é curto!')
        elif medio:
            print('Seu nome é normal!')
        else:
            print('Seu nome é muito grande!')
    else:
        print('Pelo menos duas letras')
else:
    print('Escreva somente o primeiro nome')