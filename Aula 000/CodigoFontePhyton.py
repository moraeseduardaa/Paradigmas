#solicita o numero e o input aguarda resposta
numero = int(input("Digite um numero: "))

#laco de repeticao para exibir a tabuada
for i in range(1,11):
    #calcula a tabuada conforme o numero digitado    
    resultado = numero * i
    #exibe o resultado
    print(f"{numero} x {i} = {numero * i}")
