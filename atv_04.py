'''Crie uma função que receba três notas e retorne a média do aluno.
○ Mostre se o aluno está aprovado ou reprovado (média mínima 7).'''

def media(n1, n2, n3):
    media = (n1 + n2 + n3) // 3
    return media

n1 = int(input("Diga a sua primeira nota: "))
n2 = int(input("Diga a sua segunda nota: "))
n3 = int(input("Diga a sua terceira nota: "))

resultado = media(n1, n2, n3)

if resultado >= 7:
    print(f"Voce obteve uma media de {resultado} e foi aprovado")

else:
    print(f"Voce obteve uma media de {resultado} e foi reprovado.")