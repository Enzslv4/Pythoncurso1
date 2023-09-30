# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Enzo',
    'sobrenome': 'Silva',
    'idade': 21,
    'peso': 64
}

# quantidade de chaves
# print(pessoa.__len__()) 
# ou print(len(pessoa))
chaves = ''

'''
print(pessoa.keys())
mostra as chaves

para mostrar tudo mais facilmente:
print(list(pessoa.keys()))

for chave in pessoa:
    chaves += f'{chave} '

print(chaves.rstrip(' '))
'''
# para mostrar os valores das chaves:
# print(list(pessoa.values()))

#para mostrar itens do dicionario?
#for chave, valor in pessoa.items():
    #print(chave, valor)

# caso uma chave nao exista, vc pode usar o setdefaut:
# pessoa.setdefault('agua', 0)
# print(pessoa['agua'])