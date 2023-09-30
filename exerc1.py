"""
Nome
Idade
'Seu nome é {}'
'Invertido: {}'
'Quantidade'
'Primeira letra'
'Ultima'
se nada for digitado: 'Desculpe, vc deixou campos vazios'
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Invertido: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contêm espaços')
    else:
        print('Seu nome não contêm espaços')
    
    print(f'Tem {len(nome)} caracteres')
    print(f'A primeira letra é {nome[:1]}')
    print(f'A última letra é {nome[-1:]}')
else:
    print('Desculpe, vc deixou campos vazios')