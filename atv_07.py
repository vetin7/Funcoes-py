import random
def dado(min, max):
    return random.randint(min, max)

resul = dado(1, 6)
print(f"Resultado: {resul}")
