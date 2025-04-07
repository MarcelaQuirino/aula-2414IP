#9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem 
#na carteira (em R$)
#e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,45.

dinheiro = float(input("na carteira: R$ "))
us = 3.45
comprar = dinheiro / us

print (f"com R$  {dinheiro}, voce pode comprar US$ {comprar:.2f} ")