def contagem(texto):
    contador = 0
    vogais = "aeiouáéíóúâêîôûãõàèìòùäëïöü"
    texto = texto.lower().replace(" ", "")
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

texto = input("Informe seu texto: ")
resultado = contagem(texto)
print(f"Seu texto tem {resultado} vogais.")
