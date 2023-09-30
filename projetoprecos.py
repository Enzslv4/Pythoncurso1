'''
OUTRAS REGRAS
- Caso item extra seja informado num pedido que não tenha o respectivo item principal, apresentar mensagem 
    "Item extra não pode ser pedido sem o principal".
- Combos não são considerados como item principal.
- É possível pedir mais de um item extra sem precisar de mais de um principal.
- Se não forem pedidos itens, apresentar mensagem "Não há itens no carrinho de compra!"
- Se a quantidade de itens for zero, apresentar mensagem "Quantidade inválida!".
- Se o código do item não existir, apresentar mensagem "Item inválido!"
- Se a forma de pagamento não existir, apresentar mensagem "Forma de pagamento inválida!"
'''

import os

produtos = {
    "cafe": 3,
    "chantily": 1.5,
    "suco": 6.2,
    "sanduiche": 6.5,
    "queijo": 2,
    "salgado": 7.25,
    "combo1": 9.5,
    "combo2": 7.5
}

pagamentos = (
    "debito",
    "dinheiro",
    "credito"
)



while True:
    item = input('Digite o produto: ')
    if item in produtos:
        ...
    else:
        print('Produto inválido')
        break