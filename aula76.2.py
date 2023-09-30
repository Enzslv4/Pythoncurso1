# manipulando chaves e valores em dicionarios

pessoa = {}

pessoa['nome'] = 'Enzo' 
# para criar uma nova chave mesmo depois de ter criado
# o dicionario

pessoa['idade'] = '21'

for chave in pessoa:
    print(chave, pessoa[chave])

# para apagar uma chave, basta usar o del
#del pessoa['idade']

# para tentar achar uma chave que vc n sabe se existe:
if pessoa.get('agua') is None:
    print('Essa chave nao existe')