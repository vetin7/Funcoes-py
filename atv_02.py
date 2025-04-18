'''Crie funções para converter quilômetros em milhas, metros em
centímetros e litros em mililitros.'''

def milhas(n1):
    milha = n1 * 0.621371
    return milha

def centimetros(n1):
    cent = n1 * 100
    return cent

def mililitros(n1):
    ml = n1 * 1000
    return ml

n1 = int(input("Diga o valor a ser convertido: "))
conv = input("Diga para o que ele sera convertido: ")

m = milhas(n1)

c = centimetros(n1)

ml = mililitros(n1)

if conv == "milhas":
    print(f"O valor {n1} em {conv} é igual a {m}")

elif conv == "centimetros":
    print(f"O valor {n1} em {conv} é igual a {c}")

elif conv == "mililitros":
    print(f"O valor {n1} em {conv} é igual a {ml}")

else:
    print("Comando errado :(")