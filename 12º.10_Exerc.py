#10) Faça um algoritmo que leia a largura e altura de uma parede, 
# calcule e mostre a área a ser pintada e a quantidade de tinta 
# para o serviço,
#sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

altura = float(input("altura: "))
largura = float(input("largura: "))
metro_quadrado = (largura * altura)
litro_de_tinta = (metro_quadrado * 2)

print (f"com altura  {altura} mt e largura{largura} mt, voce precisa comprar {litro_de_tinta:.2f} litros de tinta para cada demão")