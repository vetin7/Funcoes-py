def milhas(num1):
    milhas = num1 * 0.621371
    return milhas

def centimetros(num1):
    cent = num1 * 100
    return cent

def mililitros(num1):
    ml = num1 * 1000
    return ml

num1 = int(input("Diga o valor a ser convertido: "))
conv = input("Diga para o que ele sera convertido: ")

m = milhas(num1)
c = centimetros(num1)
ml = mililitros(num1)

if conv == "milhas":
    print(f"O valor {num1} em {conv} é igual a {m}")
elif conv == "centimetros":
    print(f"O valor {num1} em {conv} é igual a {c}")
elif conv == "mililitros":
    print(f"O valor {n1} em {conv} é igual a {ml}")
else:
    print("Comando errado.")
