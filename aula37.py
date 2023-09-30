"""
Repetições
while
loop infinito
continue = pula loops, mas n quebra o while(que seria o break)
"""

cont = 0

while cont <= 50:
    cont += 1
    print (cont)
    if cont == 25:
        print('Metade')

print('Acabou')