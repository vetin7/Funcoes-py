'''Crie uma função que receba uma frase e conte quantos caracteres (sem
espaço) ela possui.'''

def contagem(frase):
    return len(frase.replace(" ",""))

frase = input("Escreva a sua frase: ")

qtd = contagem(frase)

print(f"Sua frase tem um total de {qtd} caracteres.")