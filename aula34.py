"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infini
"""

condicao = input('Digite algo: ')

while condicao.isdigit:
    nome = input('Seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break

print('agua')