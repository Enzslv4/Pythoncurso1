# exercicio 2

hora = input('Que horas são? ')

try:
    num = int(hora)
    manha = (0 <= num <= 11)
    tarde = (12 <= num <= 17)
    noite = (18 <= num <= 23)
    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    elif noite:
        print('Boa noite!')
    else:
        print('Não conhço essa hora')
except:
    print('Hora inválida!')
