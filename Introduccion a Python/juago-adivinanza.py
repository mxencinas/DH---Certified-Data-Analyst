import random

numero_secreto = random.randint(1, 100)

cant_intentos = 0
cant_max_intentos = 7

print("JUEGO DE ADIVINANZA".center(35))
print(f"Tienes {cant_max_intentos} intentos.")

while True:
    
    try:
        numero_ingresado = int(input("Introducí un numero de 1 al 100: "))
    except ValueError:
        print("Ingreso invalido. Debe ingresar un numero")
        continue
    
    cant_intentos += 1

    if cant_intentos == cant_max_intentos and not numero_ingresado == numero_secreto:
        print("GAME OVER! No te quedan más intentos.")
        print(f"El número secreto era {numero_secreto}.")
        break

    if numero_ingresado == numero_secreto:
        print(f"FELICIDADES, ADIVINASTE! El numero secreto es: {numero_secreto}")
        break
    elif numero_ingresado < numero_secreto:
        print("ERROR! El numero secreto es mayor")
    else:
        print("ERROR! El numero secreto es menor")

    print(f"Te quedan {cant_max_intentos - cant_intentos} intentos")   
