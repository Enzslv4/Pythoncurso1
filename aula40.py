"""
Calculadora com while


except Exception as error:
    print error
isso mostra o erro q ocorreu
"""

while True:
    try:
        dig1 = input('Digite o primeiro numero: ')
        num1 = float(dig1)
        dig2 = input('Digite o segundo numero: ')
        num2 = float(dig2)
        operador = input('Digite o operador(+, -, *, /): ')
        
        if operador == '+':
            resultado = num1 + num2
            print(f'A soma de {dig1} e {dig2} é: {resultado}')
        elif operador == '-':
            resultado = num1 - num2
            print(f'A subtração de {dig1} e {dig2} é: {resultado}')
        elif operador == '*':
            resultado = num1 * num2
            print(f'A multiplicação de {dig1} e {dig2} é: {resultado}')
        elif operador == '/':
            resultado = num1 / num2
            print(f'A divisão de {dig1} e {dig2} é: {resultado:.2f}')
        else:
            print('Operador errado')

    except:
        print('Voce precisa digitar dois numeros!')
    sair = input('Quer [s]air? ').lower().startswith('s')
    if sair is True:
        break