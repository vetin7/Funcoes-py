'''Crie uma função que receba uma palavra e diga se ela é um palíndromo
(lê igual de frente para trás).'''

def analise(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra[::-1]

palavra = input("Diga a sua palavra: ")

invertido = analise(palavra)

if invertido == palavra:
    print(f"{palavra} é um polindromo.")

else:
    print(f"{palavra} nao é um polindromo.")