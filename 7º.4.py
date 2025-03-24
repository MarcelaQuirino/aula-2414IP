#Faca um programa que peca a idade e 
#verifique com a idade se ela é bebe, crianca, adolescente, 
#jovem, adulto ou idoso.

idade = int(input("qual é sua idade?"))

if idade <= -1:
    print("voce e bebe")
    pass
#acrescentado na correção

if idade >= 0 and idade <= 4:
    print("voce e bebe")
    pass

elif idade >= 5 and idade <= 12:
    print("voce e criança")
    pass

elif idade >= 13 and idade <= 17:
    print("voce e adolescente")
    pass

elif idade >= 18 and idade <= 20:
    print("voce e jovem")
    pass

elif idade >= 21 and idade <= 60:
    print("voce é maior de idade")
    pass

elif idade >= 61 and idade <= 99:
    print("voce e paciente Geriátrico")
    pass

else:
    print("idade do Pó")
