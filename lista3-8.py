#8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar.
#Sabendo que a decisão é sempre pelo mais barato.
print("8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.")
prod1 = int (input("Digite o valor do primeiro produto: "))
prod2 = int (input("Digite o valor do segundo produto: "))
prod3 = int (input("Digite o valor do terceiro produto: "))
if prod1 < prod2 and prod1 < prod3:
    print("Compre o primeiro produto.")
elif prod2 < prod1 and prod2 < prod3:
        print("Compre o segundo produto.")
elif prod3 < prod1 and prod3 < prod2:
            print("Compre o terceiro produto")
else: print("Você informou valores iguais.")