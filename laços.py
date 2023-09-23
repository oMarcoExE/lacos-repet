#Lista de Exercícios para Laços de Repetição

##Exercício 1 - Impressão de números
    ###Escreva um programa pque imprima numeros de 1 a 10 usando um laço for. 
    ###Refatore o código para solicitar um numero maximo de impressão ao usuario.
    ###Refatore o código para solicitar ao usuário se deve ser impresso em ordem crescente ou decrescente

max = int(input("Quantos números deseja imprimir: "))
max += 1
ord = int(input("Crescente ou decrescente? (1 = >  2 = <): "))

if ord == 1:
    print("Crescente: \n")
    for num in range(1, max):
        print(num)

elif ord == 2:
    print("Descrescente: \n")
    for num in range(max, 0, -1):
        print(num)