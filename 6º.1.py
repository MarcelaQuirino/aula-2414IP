#Faca um programa que peca a idade e 
#verifique com a idade se ela é crianca, adolescente, jovem, adulto ou idoso.
#and or not

idade = int(input("qual é sua idade?"))

if idade <= 12:
    print("voce e criança")
    pass

elif idade > 12:
    print("voce e adolescente")
    pass

elif idade < 18:
    print("voce e adolescente")
    pass

elif idade >= 18:
    print("voce e jovem")
    pass

elif idade >= 21:
    print("voce é maior de idade")
    pass

elif idade < 21:
    print("voce e jovem")
    pass

elif idade >= 60:
    print("voce e idoso")
    pass

else:
    print("idade invalida")
    pass