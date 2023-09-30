"""
operadores logicos
and - e
or - ou
not - nao
and - todas as condições precisam ser verdadeiras
or - pelo menos uma

sao considerados 'falsy' os valores:
0, 0.0, '' e False

Tambem existe o valor 'None'
usado para representar um não valor
"""
entrada = input('[E]ntrar ou [S]air: ')
senhad = input('Senha: ')
senhaperm = '123456'

if (entrada == 'E' or entrada == 'e') and senhad == senhaperm:
    print('Entrar')
else:
    print('Sair')