def carac(frase):
    return len(frase.replace(" ",""))

frase = input("Escreva a sua frase: ")
num = carac(frase)
print(f"Sua frase tem um total de {num} caracteres.")
