''' Crie funções para soma, subtração, multiplicação e divisão.
Faça um programa que peça dois números e mostre o resultado da
operação escolhida. '''

def soma(n1, n2):
    adicao = n1 + n2
    return adicao

def sub(n1, n2):
   subtracao = n1 - n2
   return subtracao

def mult(n1, n2):
   vezes = n1 * n2
   return vezes

def div(n1, n2):
   divisao = n1 // n2
   return divisao
    
n1 = int(input("Diga o primeiro numero: "))
n2 = int(input("Diga o segundo numero: "))
operacao = input("Diga a operacao a ser feita: ")

s = soma(n1, n2)

t = sub(n1, n2)

v = mult(n1, n2)

d = div(n1, n2)

if operacao == "soma":
 print(f"A soma entre {n1} e {n2} é {s}.") 

elif operacao == "subtracao":
   print(f"A subtracao entre {n1} e {n2} é {t}.")

elif operacao == "multiplicacao":
   print(f"A multiplicacao entre {n1} e {n2} é {v}.")

elif operacao == "divisao":
   print(f"A divisao entre {n1} e {n2} é {d}.")

else:
   print("Erro, operação invalida.")