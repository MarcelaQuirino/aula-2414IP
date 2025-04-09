#14) A locadora de carros precisa da sua ajuda para cobrar seus serviços.
#Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço total a pagar,sabendo que o carro custa 
#R$90 por dia e 
#R$0,20 por Km rodado

km = float(input("Kms rodados: "))
dias = float(input("Dias com o carro: "))

km_rodado = (km * 0.20)
diária = (dias * 90)
locação = (km_rodado + diária)
print(f"Total a pagar: {locação}")