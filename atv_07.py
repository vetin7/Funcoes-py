'''Crie uma função que gere um número aleatório entre 1 e 6, simulando o
lançamento de um dado.'''

import random

def dado(min, max):
    return random.randint(min, max)

n = dado(1, 6)

print(f"O dado girou e um {n} apareceu.")