def tabuada(num1):
    for i in range(1, 11): 
        print(f"{num1} x {i} = {num1 * i}")

num1 = int(input("Diga o numero: "))
tabuada(num1)
