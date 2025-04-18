def media(num1, num2, num3):
    media = (num1 + num2 + num3) // 3
    return media

num1 = int(input("Diga a sua primeira nota: "))
num2 = int(input("Diga a sua segunda nota: "))
num3 = int(input("Diga a sua terceira nota: "))

resultado = media(num1, num2, num3)

if resultado >= 7:
    print(f"Voce foi aprovado")
else:
    print(f"Voce foi reprovado.")
