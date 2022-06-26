from time import sleep
from math import sqrt

print("------------------------------------------")
sleep(1)
print("            EQUAÇÃO DO 2º GRAU")
sleep(1)
print("------------------------------------------")
sleep(2)

while True:
    a = int(input("Digite o valor de a: "))
    sleep(1)
    b = int(input("Digite o valor de b: "))
    sleep(1)
    c = int(input("Digite o valor de c: "))
    sleep(2)

    delta = (b**2) - (4*a*c)

    print("------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)

    if delta < 0:
        print("------------------------------------------")
        sleep(1)
        print("           NÃO HÁ RAÍZES REAIS")
        sleep(2)

    if delta == 0:
        print("------------------------------------------")
        sleep(1)
        print("                RAIZ ÚNICA")
        sleep(1)
        print("------------------------------------------")
        sleep(2)

        raiz_quadrada = sqrt(delta)
        raiz_unica = (-(b) + raiz_quadrada) / (2 * a)

        print(f"Raiz: {raiz_unica}.")
        sleep(2)

    if delta > 0:
        print("------------------------------------------")
        sleep(1)
        print("               DUAS RAÍZES")
        sleep(1)
        print("------------------------------------------")
        sleep(2)

        raiz_quadrada = sqrt(delta)

        primeira_raiz = (-(b) + raiz_quadrada) / (2 * a)
        segunda_raiz = (-(b) - raiz_quadrada) / (2 * a)

        print(f"Primeira Raiz: {primeira_raiz}.")
        sleep(1)
        print(f"Segunda Raiz: {segunda_raiz}.")
        sleep(2)
    
    print("------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)

    print("------------------------------------------")
    sleep(1)
    continuar = str(input("Quer digitar outra equação? ")).strip().upper()[0]
    sleep(1)

    if continuar == "N":
        print("------------------------------------------")
        sleep(1)

        print(" ")
        sleep(2)

        print("------------------------------------------")
        sleep(1)
        print("            PROGRAMA ENCERRADO")
        sleep(1)
        print("------------------------------------------")

        sleep(1)
        break
    
    if continuar == "S":
        print("------------------------------------------")
        sleep(1)

        print(" ")
        sleep(2)

        print("------------------------------------------")
        sleep(2)
sleep(2)
