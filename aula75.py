# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

    
por_2 = criar_multiplicador(2)
por_3 = criar_multiplicador(3)
por_4 = criar_multiplicador(4)

print(por_2(3))
print(por_3(3))
print(por_4(3))