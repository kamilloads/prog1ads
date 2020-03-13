#5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
#O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

valor_o = float(input("Digite o valor original da dívida: "))
dias_atraso = int(input("Digite a quantidade de dias em atrasado: "))
valor_dias = float(input("Digite o valor da multa por dias de atraso: "))
valor_f = valor_o + dias_atraso * valor_dias
print (f"O valor a ser pago é: {valor_f}")
