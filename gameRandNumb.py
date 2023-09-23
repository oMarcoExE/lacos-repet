from random import randint

rand = randint(1, 100)
num = 0
tentativas = 0

while num != rand:
    num = int(input("Digite numero: "))
    tentativas += 1
    if num > rand: print("Seu numero é maior")
    elif num < rand: print("Seu numero é menor")
    elif num == rand: print(f"Parabéns!! Você acertou em {tentativas} tentativas")