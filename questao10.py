#10. Faça um programa que calcula o novo valor do salário de um funcionário.
#O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario = float(input("Digite o valor do seu salário atual: "))
reajuste = float(input("Digite o valor do percentual do reajuste: "))
salario_final = ((reajuste+100)/100)*salario
print(f"Seu salario será de {salario_final}")
