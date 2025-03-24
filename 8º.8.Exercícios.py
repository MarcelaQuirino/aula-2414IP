#8) Desenvolva um programa que leia uma distância em metros e mostre 
#os valores relativos em outras medidas.
#Ex:
#Digite uma distância em metros: 185.72
#A distância de 85.7m corresponde a:
#0.18572Km
#1.8572Hm
#18.572Dam

metros = float(input("Digite a distância em metros"))

km = metros / 1000
cm = metros * 100
mm = metros * 1000

print(f"A distancia de {metros} metros corresponde a: ")
print(f"{km} quilômetros")
print(f"{cm} centímetros")
print(f"{mm} milímetros")