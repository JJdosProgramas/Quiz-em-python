import random
numb = random.randrange(101)
guess=101
tentativas = 0
print("Adivinhe o numero de 1 a 100")
while guess != numb:
    guess = input("Digite um numero ")
    tentativas+=1
    if guess.isdigit():
        guess = int(guess)
        if guess>numb:
            print("O numero é menor")
        elif guess<numb:
            print("O numero é maior")
    else: 
        print("digite um numero na proxima vez")
        quit()
    

if guess == numb:
    print("Parabéns você ganhou!!")
    print("Você acertou em" ,tentativas, "tentativas")