#while => enquanto
#for => para

#Exemplo 1 : Contador Simples

#.contador = 0
#.while contador < 5:
 #.   print(f"contagem: {contador}")
  #.  contador +=1

#.Exemplo2: Solicitando input até que seja correto
#.sinal = significa diferente
#!= diferença

#.senha = "1234"
#.tentativa = ""
#.while tentativa != senha:
    #.tentativa = input("Digite a Senha: ")
#.print("Acesso concedido!")

#Exemplo 3: Loop Infinito com Interrupção
# .lower coloca todas as letras em minusculas e .uppr em maiúsculas
#ctrl=Z Desfazer
#== sign igualdade
#true sign verdadeiro

while True:
    comando = input("digite 'sair' para parar: ")
    if comando.lower () == "sair" :
        print("Até a proxima")
        break
    print(f"Você digitou: {comando}")

    #Próxima aula for
