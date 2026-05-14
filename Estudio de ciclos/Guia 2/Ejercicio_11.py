secreto = 19
num = 0
intentos = 0

while num != secreto:
    intentos += 1
    num = int(input("Ingrese un numero para adivinar: "))
    if num != secreto:
        print("No es el nuemero correcto, intentelo de nuevo")
        if intentos >= 3:
            print("lo siento, ya lo intento mas de 3 veces, perdio el juego")
            break
else:
    print(f"Felcicidades, lo hizo al {intentos} intento")