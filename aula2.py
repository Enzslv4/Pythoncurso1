# sep= serve para separar argumentos
# end= serve para determinar o final do print
# \r\n -> CRLF (forma de quebrar linha)
# \n -> LF

print(12, 34, sep='-', end='\r\n')
print(56, 78, sep='-', end=('\n'))
print('edsa', 'fsd', sep='-', end=('\n##')) 
# com o \n no inicio, ele da kill na linha e pula pra outra começando com ##
print('qwerty', 'fff', sep='-', end=('##\n'))
# nesse caso ele mostra o ## primeiro e dps termina a linha