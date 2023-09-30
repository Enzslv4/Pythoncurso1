'''
split e join com list e str
split - divide uma string
join - une uma string
strip - corta espaços do começo e do fim da string
'''

frase = 'olha que coisa mais linda, mais cheia de graça'
lista = frase.split(',') # split sem argumento sepera por espaços


for i, frase in enumerate(lista):
    print(lista[i].strip())

frases_unidas = '-'.join(lista)
print(frases_unidas)