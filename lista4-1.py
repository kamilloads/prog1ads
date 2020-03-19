#1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#-- salários até R$ 280,00 (incluindo) : aumento de 20%
#-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#-- o salário antes do reajuste;
#-- o percentual de aumento aplicado;
#-- o valor do aumento;
#-- o novo salário, após o aumento.
salario = float(input("Informe o valor em reais do seu salário: "))
if salario <= 280:
    salario_final = ((20+100)/100)*salario
    aumento = salario_final * 0.2
    print (f"O salário de {salario} recebeu um valor aplicado {aumento} que é igual a 20% do salário e seu novo salário é de {salario_final}.")
elif salario <=700 and salario > 280:
    salario_final = ((15+100)/100)*salario
    aumento = salario_final * 0.15
    print(f"O salário de {salario} recebeu um valor aplicado {aumento} que é igual a 15% do salário e seu novo salário é de {salario_final}.")
elif salario <=1500 and salario > 700:
    salario_final = ((10+100)/100)*salario
    aumento = salario_final * 0.1
    print(f"O salário de {salario} recebeu um valor aplicado {aumento} que é igual a 10% do salário e seu novo salário é de {salario_final}.")
elif salario >1500:
    salario_final = ((15+100)/100)*salario
    aumento = salario_final * 0.05
    print(f"O salário de {salario} recebeu um valor aplicado {aumento} que é igual a 5% do salário e seu novo salário é de {salario_final}.")