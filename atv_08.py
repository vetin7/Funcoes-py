def analise(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra[::-1]

palavra = input("Informe a palavra: ")
invertido = analise(palavra)
if invertido == palavra:
    print(f"{palavra} é um polindromo.")
else:
    print(f"{palavra} nao é um polindromo.")
