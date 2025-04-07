#11) Desenvolva uma lógica que leia os valores de A, B e C 
#de uma equação do segundo grau e mostre o valor de Delta.
#Delta = b2 – 4ac

a = float(input("Digite o valor 1: "))
b = float(input("Digite o valor 2: "))
c = float(input("Digite o valor 3: "))
delta = (b * b) - 4 * a * c

print(f"Delta é: {delta}")