"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 # se caso eu defina a var fora do escopo, posso acessar essa var

def escopo():
    # global x - se eu quisesse q o x de fora valesse dentro
    x = 10
    print(x)
    def dentro():
        x = 11
        y = 2
        print(x, y)
    
    dentro()
    print(x)


print(x)
escopo()


# print(x) nao funcionaria pq o x esta dentro do escopo
# da funcão escopo
escopo()