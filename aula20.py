val1 = input('Digite um valor: ')
val2 = input('Digite outro: ')

if int(val1 > val2):
    print(f'O valor 1({val1}) é maior que o valor 2({val2})')
elif int(val1 < val2):
    print(f'O valor 1({val1}) é menor que o valor 2({val2})')
elif int(val1 == val2):
    print(f'O valor 1({val1}) é igual ao valor 2({val2})')
