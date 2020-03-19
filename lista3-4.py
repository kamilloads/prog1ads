#4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Digite uma letra: "))

if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U" :
    print (f"{letra} é uma vogal.")
else:
    print (f"{letra} é uma consoante.")