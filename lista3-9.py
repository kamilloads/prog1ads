#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.")
num1 = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))
num3 = int (input("Digite o terceiro numero: "))
if num1 > num2 and num1 > num3 and num2  > num3:
    print(f"{num1}, {num2}, {num3} é a ordem decrescente dos numeros.")
elif num1 > num2 and num1 > num3 and num3  > num2:
    print(f"{num1}, {num3}, {num2} é a ordem decrescente dos numeros.")
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f"{num2}, {num3}, {num1} é a ordem decrescente dos numeros.")
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"{num2}, {num1}, {num3} é a ordem decrescente dos numeros.")
elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f"{num3}, {num2}, {num1} é a ordem decrescente dos numeros.")
elif num3 > num1 and num3 > num2 and num1 > num2:
     print(f"{num3}, {num1}, {num2} é a ordem decrescente dos numeros.")
else: print("Voce digitou todos os numeros iguais ou dois3 numeros iguais.")
