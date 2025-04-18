'''Crie uma função que receba um número e imprima a tabuada desse
número.'''

def tabuada(n1):
    print(f"Tabuada do {n1}:")
    for i in range(1, 11): 
        print(f"{n1} x {i} = {n1 * i}")

n1 = int(input("Diga o numero: "))
tabuada(n1)