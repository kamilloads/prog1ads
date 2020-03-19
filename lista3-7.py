#7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
print("7 - Faça um Programa que leia três números e mostre o maior e o menor deles.")
num1 = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))
num3 = int (input("Digite o terceiro numero: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior numero.")
elif num2 > num1 and num2 > num3:
        print(f"{num2} é o maior numero.")
elif num3 > num1 and num3 > num2:
            print(f"{num3} é o maior numero.")
else: print("Voce digitou todos numeros iguais ou os dois maiores numeros iguais.")
if num1 < num2 and num1 < num3:
    print(f"{num1} é o menor numero.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} é o menor numero.")
elif num3 < num1 and num3 < num2:
    print(f"{num3} é o menor numero.")
else: print("Você digitou todos numeros iguais ou os dois menores numeros iguais")
