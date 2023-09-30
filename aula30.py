"""
formas de deixar mais simples o codigo
CONSTANTE = "Variáveis" que não vão mudar(MAIÚSCULO)
Muitas condições no mesmo if = ruim
    <- Contagem de complexidade = ruim
"""

velocidade = 60
localcar = 100

RADAR1 = 60
LOCAL1 = 100
RANGERAD = 1

velmulta = velocidade > RADAR1
multar = localcar >= (LOCAL1 - RANGERAD) and\
    localcar <= (LOCAL1 + RANGERAD)

if velmulta:
    print('Passou da velocidade')
if multar and velmulta:
    print('Multado, f :(')
else:
    print('Tá safe meu piva')