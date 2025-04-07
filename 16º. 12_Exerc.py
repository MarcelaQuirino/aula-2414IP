#12) Crie um programa que leia o preço de um 
# produto, calcule e mostre o seu
#PREÇO PROMOCIONAL, com 5% de desconto.

#Variáveis
#ni, desc, no total: real;
 
n1 = float(input("Digite o valor do produto: "))
 
desconto = (n1 * 0.05)
total =  (n1 - desconto)
print(f"preço com Desconto:{total}")