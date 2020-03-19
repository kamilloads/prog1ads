#10 - Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem (Bom Dia!), (Boa Tarde!) ou (Boa Noite!) ou (Valor Inválido!), conforme o caso.")
msg = str(input("Digitar M-matutino ou V-Vespertino ou N- Noturno: "))
if msg == "m" or msg == "M":
    print("Bom Dia!")
elif msg == "v" or msg == "V":
    print("Boa Tarde!")
elif msg == "n" or msg == "N":
    print("Boa Noite!")
    