#2. Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros de água.
#Sabendo que em 1 m3 de água há 1.000 litros, calcule quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico de água?
#Informar o tempo de banho e calcular quantos banhos precisa para consumir 1000m cubicos de agua.
tempo_banho = int(input("quantos minutos você demora no banho: "))
litros_minuto = 9
litros_calc = tempo_banho * litros_minuto
banhos = 1000/litros_calc
print(f"São nescessarios {banhos:.2f} banhos para consumir 1000 metros cúbicos de água.")
