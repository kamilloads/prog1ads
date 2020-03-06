#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00).
#Calcule quantos litros de combustível o usuário obterá com esses valores.
valor_litro_combustivel = float(input("Digite o valor do litro do combustivel: "))
valor_abastecer = float(input("Digite o valor em dinheiro que deseja abastecer: "))
valor_final = valor_abastecer / valor_litro_combustivel
print(f"A quantidade abestecida em litros foi: {valor_final}")
