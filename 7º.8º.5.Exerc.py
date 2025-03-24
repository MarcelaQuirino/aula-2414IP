#Calculadora de IMC
#imc = peso / (altura * altura)

peso = float(input( "qual seu peso?"))
altura = float(input( "qual sua altura?"))
imc = peso / (altura * altura)
print(imc)

if imc >= 0 and imc <= 18.4: #linha corrigida pelo professor
    print("Alta Inanição")
    pass

elif imc >= 18.5 and imc <= 24.9:
    print("Peso adequado á Altura")
    pass

elif imc >= 25 and imc <= 30:
    print("Sobrepeso")
    pass

elif imc >= 31 and imc <= 35:
    print("Obesidade I")
    pass

elif imc >= 36 and imc <= 40:
    print("Obesidade II")
    pass

elif imc >= 41:
    print("Obesidade III")
    pass

else:
    print("Dados Inválidos. Digite novamente: ")