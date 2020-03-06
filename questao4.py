#4. Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus Celsius e exiba o resultado.

temp_f = float(input("Digite a temperatura em fahrenheit: "))
temp_c = (temp_f - 32) * 5 / 9
print(f"A temperatura em celsius é: {temp_c} °Celsius")
