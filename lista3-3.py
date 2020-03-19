#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
gen = str (input("Digite (F) ou (M): "))
if gen == "f":
    print("Sexo Feminino")
elif gen == "m":
    print("Sexo Masculino")