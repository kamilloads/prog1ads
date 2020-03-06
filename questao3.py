#3. Faça um programa que calcule a média de consumo de combustível de um veículo.
#O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km_inicial = float(input("Digite o valor inicial da quilometragem: "))
km_final = float(input("Digite o valor final da quilometragem: "))
litros_gastos = float(input("Digite quantos litros foram gastos: "))
media = (km_final - km_inicial) / litros_gastos
print(f"A media de consumo de combustivel foi: {media} litros gastos")
