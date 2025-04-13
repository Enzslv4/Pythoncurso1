# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def createFunction(func):
    def intern(*args, **kwargs):
        for arg in args:
            isString(arg)
            result = func(*args, **kwargs)
            return result
    return intern

def invertString(string):
    return string[::-1]

def isString(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string. ')

invertStringCheckParam = createFunction(invertString)
inverted = invertStringCheckParam('Enzo')
print(inverted)