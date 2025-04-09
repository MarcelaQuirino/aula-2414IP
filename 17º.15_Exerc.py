#15) Crie um programa que leia o número de dias trabalhados em um mês 
#e mostre o salário de um funcionário, sabendo que ele 
#trabalha 8 horas por dia e ganha R$25 por hora trabalhada.

dias = float(input("Dias trabalhados no mês: "))
diaria = (8 * 25)
Salario = (dias * diaria)

print(f"Este mês seu salário será: R${Salario} ")