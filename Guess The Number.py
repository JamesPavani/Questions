from time import sleep
from random import randint

placar_jogador = 0
placar_computador = 0
número_computador = randint(1, 10)
cont_tentativas = 1

print("-----------------------------------------------------------")
sleep(1)
print("                    ADVINHE O NÚMERO")
sleep(1)
print("-----------------------------------------------------------")
sleep(1)

print("Hoje vamos jogar um jogo!")
sleep(2)
print("Estou pensando em um número entre 0 e 11.")
sleep(2)
print("Você terá que acertar que número é esse...")
sleep(2)
print("Mas saiba!")
sleep(2)
print("Você só tem 3 tentativas!")
sleep(2)
print("Vamos nessa!")
sleep(2)

print("-----------------------------------------------------------")

print(" ")
sleep(2)

while True:
    print("-----------------------------------------------------------")
    sleep(1)
    número_jogador = int(input("Em que número estou pensando? "))
    sleep(1)
    print("-----------------------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)

    while True:
        if número_jogador != número_computador:

            print("-----------------------------------------------------------")
            sleep(2)
            print("Eu não estou pensando nesse número!")
            sleep(2)
            if número_computador > número_jogador:
                print("Eu estou pensando em um número maior.")
            
            if número_computador < número_jogador:
                print("Eu estou pensando em um número menor.")

            sleep(2)
            print("Tente de novo!")
            sleep(2)
            print("-----------------------------------------------------------")
            sleep(2)

            print(" ")
            sleep(2)

            print("-----------------------------------------------------------")
            sleep(1)
            número_jogador = int(input("Em que número estou pensando? "))
            sleep(1)
            print("-----------------------------------------------------------")
            sleep(2)

            print(" ")
            sleep(2)

            if número_jogador == número_computador:
                print("-----------------------------------------------------------")
                sleep(1)
                print("VOCÊ ACERTOU!")
                sleep(1)
                print("MEUS PARABÉNS!")
                sleep(1)
                print("-----------------------------------------------------------")
                sleep(2)

                print(" ")
                sleep(2)

                placar_jogador += 1          
                break


            cont_tentativas += 1

        if cont_tentativas == 3:
            print("-----------------------------------------------------------")
            sleep(2)
            print("Você já tentou 3 vezes!")
            sleep(2)
            print(f"Eu estava pensando no número: {número_computador}.")
            sleep(2)
            print("VOCÊ PERDEU!")
            sleep(2)
            print("-----------------------------------------------------------")
            sleep(2)

            print(" ")
            sleep(2)

            placar_computador += 1

            break

        if número_jogador == número_computador:
            print("-----------------------------------------------------------")
            sleep(1)
            print("VOCÊ ACERTOU!")
            sleep(1)
            print("MEUS PARABÉNS!")
            sleep(1)
            print("-----------------------------------------------------------")
            sleep(2)

            print(" ")
            sleep(2)
                
            placar_jogador += 1          
            break


    print("-----------------------------------------------------------")
    sleep(1)
    print("                        PLACAR")
    sleep(1)
    print("-----------------------------------------------------------")
    sleep(1)

    print(f"JOGADOR: {placar_jogador}")
    sleep(1)
    print(f"COMPUTADOR: {placar_computador}")       
    sleep(1)

    print("-----------------------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)
    
    print("-----------------------------------------------------------")
    sleep(1)
    continuar = str(input("Quer continuar? ")).strip().upper()[0]
    sleep(1)
    print("-----------------------------------------------------------")
    sleep(2)

    while continuar != "S" and continuar != "N":
        print(" ")
        sleep(2)

        print("-----------------------------------------------------------")
        sleep(1)
        print("Não entendi.")
        sleep(2)
        print("Por favor, digite de novo!")
        sleep(2)
        continuar = str(input("Quer continuar? "))[0].strip().upper()
        sleep(2)
        print("-----------------------------------------------------------")
        sleep(2)
    
    if continuar == "S":
        print(" ")
        sleep(2)

        print("-----------------------------------------------------------")
        sleep(1)
        print("Ok, vamos de novo.")
        sleep(1)
        print("-----------------------------------------------------------")
        sleep(2)

        print(" ")
        sleep(2)

        cont_tentativas = 1

        número_computador = randint(0, 10)
    
    else:
        print(" ")
        sleep(2)
        print("-----------------------------------------------------------")
        sleep(1)
        print("Ok, obrigado por jogar!")
        sleep(1)
        print("-----------------------------------------------------------")
        sleep(2)
        break

print(" ")
sleep(2)

print("-----------------------------------------------------------")
sleep(1)
print("                    PLACAR FINAL")
sleep(1)
print("-----------------------------------------------------------")
sleep(1)

print(f"JOGADOR: {placar_jogador}")
sleep(1)
print(f"COMPUTADOR: {placar_computador}")
        
sleep(1)

print("-----------------------------------------------------------")
sleep(2)

print(" ")
sleep(2)

print("-----------------------------------------------------------")
sleep(2)

if placar_computador > placar_jogador:
    print("RESULTADO: COMPUTADOR VENCEDOR!")

elif placar_computador == placar_jogador:
    print("RESULTADO: EMPATE!")

else:
    print("RESULTADO: JOGADOR VENCEDOR!")

sleep(2)
print("-----------------------------------------------------------")
sleep(2)
