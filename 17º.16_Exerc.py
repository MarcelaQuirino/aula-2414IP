#16) [DESAFIO] Escreva um programa para calcular a 
#redução do tempo de vida de um fumante. Pergunte a quantidade de 
#cigarros fumados por dias e quantos anos ele já fumou. 
#Considere que um fumante perde 10 min de vida a cada cigarro.
#Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
#PASSO 02 - CONDIÇÕES BÁSICAS

cigarros_dia = float(input("Quantos cigarros voce fuma ao dia: "))
fumante_anos = float(input("Há quantos anos voce fuma: "))

menos_vida = (cigarros_dia * 10)
#24 horas/10 minutos = 144 minutos = 24 horas
