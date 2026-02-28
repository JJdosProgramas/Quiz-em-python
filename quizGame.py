print("Bem vindo ao meu quiz")

acertou = 0 
jogar = input("Quer jogar? ")
if jogar.lower() == "sim" or jogar == "s":
    print("Boa")
else:
    quit()

pergunta1 = input("Qual país sede da copa do mundo de 2014? ")   
if pergunta1.lower()  == "brasil":
    print("correto")
    acertou+=1
else:
    print("errou")
pergunta2 = input("Quem foi o primeiro presidente do Brasil? ")
if pergunta2.lower()  == "marechal deodoro da fonseca" or pergunta2 =="deodoro da fonseca":
    print("correto")
    acertou+=1
else:
    print("errou")

pergunta3 = input("Quem é o atual presidente do Brasil(2022-2026)? ")   
if pergunta3.lower()  == "Lula" or pergunta3 == "lula":
    print("correto")
    acertou+=1
else:
    print("errou")

pergunta4 = input("Qual o cantor responsavel pela musica Asa Branca? ")   
if pergunta4.lower()  == "Luiz Gonzaga" or pergunta4 == "luiz gonzaga":
    print("correto")
    acertou+=1
else:
    print("errou")

print("Você acertou:" ,acertou)
print("Você acertou: " + str((acertou/4) * 100) + "%")