import random
kino_usuario = []
kino_al = []
menu_bool = False
ganadores = 0
premio = 400_000
gano = False
while not menu_bool:
    print("1. Comprar kino")
    print("2. Revisar pozo")
    print("3. Retirar premio")
    print("4. Salir")
    
    try: 
        opt= int(input("Ingrese la opcion: "))
    except ValueError:
        print("Error, Ingrese un numero entero")
    else:
        if opt == 1:
            kino_usuario = []
            gano = False
            ganadores = 0
            while len(kino_usuario) < 14:
                num_usuario = int(input("Ingrese los numeros de su kino: "))
                if 1 <= num_usuario <= 24:
                    if num_usuario not in kino_usuario:
                        kino_usuario.append(num_usuario)
                    else:
                        print("Error, tiene que ingresar un numero del 1 al 24 y no se pueden repetir")                    
                print(f"Su kino es: {kino_usuario}")
            

            for i in range(14):
                kino_al = random.sample(range(1,25),14)
                if i not in kino_al:               
                    kino_al.append(i)
            print(f"Cartola ganadora: {kino_al}")
            for num in kino_usuario:
                if num in kino_al:
                    ganadores += 1
            if ganadores == 14:
                print("Felicidades ganaste el kino!")
                gano = True
            else:
                print("Por desgracia no gano el kino")
            print(f"tuvo: {ganadores} aciertos")
        elif opt == 2:
            print(f"Premio: {premio}")
        elif opt == 3:
            if gano == True:
                print("Felicidades, su premio ha sido retirado")
            else:
                print("Lo siento, no ha ganado")
        elif opt == 4:
            print("Adios")
            menu_bool = True
                    

                