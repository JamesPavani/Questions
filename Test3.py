from time import sleep

print("--------------------------------------------------------")
sleep(1)
print("              CONVERSOR DE TEMPERATURAS")
sleep(1)
print("--------------------------------------------------------")
sleep(2)

print(" ")
sleep(2)

while True:
    print("--------------------------------------------------------")
    sleep(1)
    print("[1] - Celsius para Fahrenheit.")
    sleep(1)
    print("[2] - Celsius para Kelvin.")
    sleep(1)
    print("[3] - Fahrenheit para Celsius.")
    sleep(1)
    print("[4] - Fahrenheit para Kelvin.")
    sleep(1)
    print("[5] - Kelvin para Celsius.")
    sleep(1)
    print("[6] - Kelvin para Fahrenheit.")
    sleep(1)
    print("--------------------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)

    print("--------------------------------------------------------")
    sleep(1)
    opção = int(input("Digite a opção da conversão que deseja realizar: "))
    sleep(1)
    print("--------------------------------------------------------")
    sleep(2)

    while opção < 1 or opção > 6:
        print(" ")
        sleep(2)

        print("--------------------------------------------------------")
        sleep(1)
        print("OPCÃO INVÁLIDA!!!!!!")
        sleep(1)
        print("Por favor, digite de novo!")
        sleep(1)
        opção = int(input("Digite a opção da conversão que deseja realizar: "))
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)
    
    print(" ")
    sleep(2)

    print("--------------------------------------------------------")
    sleep(1)
    temperatura = float(input("Digite o valor que deseja converter: "))
    sleep(1)
    print("--------------------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)

    if opção == 1:

        Celsius_Fahrenheit = (temperatura * 1.8) + 32

        print("--------------------------------------------------------")
        sleep(1)
        print(f"Resultado da Conversão: {Celsius_Fahrenheit}ºF.")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

    if opção == 2:

        Celsius_Kelvin = (temperatura + 273.15)

        print("--------------------------------------------------------")
        sleep(1)
        print(f"Resultado da Conversão: {Celsius_Kelvin}K.")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

    if opção == 3:

        Fahrenheit_Celsius = (temperatura - 32) / 1.8

        print("--------------------------------------------------------")
        sleep(1)
        print(f"Resultado da Conversão: {Fahrenheit_Celsius}ºC.")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

    if opção == 4:

        Fahrenheit_Kelvin = ((temperatura - 32) / 1.8) + 273.15

        print("--------------------------------------------------------")
        sleep(1)
        print(f"Resultado da Conversão: {Fahrenheit_Kelvin}K.")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

    if opção == 5:

        Kelvin_Celsius = (temperatura - 273.15)

        print("--------------------------------------------------------")
        sleep(1)
        print(f"Resultado da Conversão: {Kelvin_Celsius}ºC.")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

    if opção == 6:

        Kelvin_Fahrenheit = ((temperatura - 273) * 1.8) + 32

        print("--------------------------------------------------------")
        sleep(1)
        print(f"Resultado da Conversão: {Kelvin_Fahrenheit}ºF.")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)
    
    print(" ")
    sleep(2)

    print("--------------------------------------------------------")
    sleep(1)
    continuar = str(input("Deseja realizar outra Conversão? ")).strip().upper()[0]
    sleep(1)
    print("--------------------------------------------------------")
    sleep(2)

    print(" ")
    sleep(2)

    while continuar != "S" and continuar != "N":
        print("--------------------------------------------------------")
        sleep(1)
        print("Não entendi.")
        sleep(1)
        print("Por favor, responda novamente.")
        sleep(1)
        continuar = str(input("Deseja realizar outra Conversão? ")).strip().upper()[0]
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

        print(" ")
        sleep(2)

    if continuar == "S":
        pass

    if continuar == "N":
        print("--------------------------------------------------------")
        sleep(1)
        print("                 PROGRAMA ENCERRADO")
        sleep(1)
        print("--------------------------------------------------------")
        sleep(2)

        break
sleep(2)
