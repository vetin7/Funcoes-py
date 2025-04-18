def soma(num1, num2):
    soma = num1 + num2
    return soma

def sub(num1, num2):
   subtracao = num1 - num2
   return subtracao

def mult(num1, num2):
   mult = num1 * num2
   return mult

def div(num1, num2):
   divisao = num1 // num2
   return divisao
    
num1 = int(input("Diga o primeiro numero: "))
num2 = int(input("Diga o segundo numero: "))
operacao = input("Diga a operacao a ser feita: ")

so = soma(num1, num2)
sub = sub(num1, num2)
mul = mult(num1, num2)
div = div(num1, num2)

if operacao == "soma":
 print(f"A soma entre {num1} e {num2} é {so}.") 
elif operacao == "subtracao":
   print(f"A subtracao entre {num1} e {num2} é {sub}.")
elif operacao == "multiplicacao":
   print(f"A multiplicacao entre {num1} e {num2} é {mul}.")
elif operacao == "divisao":
   print(f"A divisao entre {num1} e {num2} é {div}.")
else:
   print("Erro, operação invalida.")
