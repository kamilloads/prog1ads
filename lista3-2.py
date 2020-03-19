#2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num = float (input("digite um numero: "))
if num > 0:
    print(f"{num} é um numero positivo.")
elif num < 0:
    print(f"{num} é um numero negativo.")
else:
    print(f"{num} é nulo")
