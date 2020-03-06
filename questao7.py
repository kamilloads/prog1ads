#7. Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos.
#O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.

larg1 = float(input("Digite a largura do cômodo 1: "))
comp1 = float(input("Digite o comprimento do cômodo 1: "))
com1 = larg1*comp1
larg2 = float(input("Digite a largura do cômodo 2: "))
comp2 = float(input("Digite o comprimento do cômodo 2: "))
com2 = larg2*comp2
larg3 = float(input("Digite a largura do cômodo 3: "))
comp3 = float(input("Digiteo o comprimento do cômodo 3: "))
com3 = larg3*comp3
larg4 = float(input("Digite a largura do cômodo 4: "))
comp4 = float(input("Digite o comprimento do cômodo 4: "))
com4 = larg4 * comp4
m2 = com1+com2+com3+com4
print(f"a area total da casa com 4 cômodos é: {m2} metros quadrados")
