import importlib

import aula98_m # singleton: só importa uma vez, por isso o for nao funciona para esse comando

for i in range(10):
    importlib.reload(aula98_m)