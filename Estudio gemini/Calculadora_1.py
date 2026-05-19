print("########Calculadora#########")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
opcion = int(input("Ingrese una opcion: "))
resultado = 0
resta = 0
while opcion != 5:
    match opcion:
        case 1:
            suma_exitosa = False
            while not suma_exitosa:
                try:
                    cantidad = int(input("Ingrese la cantidad de numeros que desea sumar: "))
                    for i in range(cantidad):
                        numero = int(input(f"Ingrese el {i+1}° numero: "))
                        resultado = resultado + numero
                    print(f"El resultado de la suma es: {resultado}")
                    suma_exitosa = True
                except ValueError:
                    print("Solo se permite el ingreso de numeros")
        case 2:
            resta_exitosa = False
            while not resta_exitosa:
                try:
                    cantidad = int(input("Ingrese la cantidad de numeros que desea restar: "))
                    if cantidad < 1:
                        print("Debe ingresar al menos 1 numero")
                        continue
                    primer_numero = int(input(f"Ingrese el 1° numero: "))
                    resultado = primer_numero

                    for i in range(2, cantidad +1):
                        numero = int(input(f"Ingrese el {i}° de {cantidad} numeros: "))
                        resultado -= numero
                    print(f"El resultadode la resta es: {resultado}")
                    resta_exitosa = True
                except ValueError:
                    print("Solo se permite el ingreso de numeros")
        case 3:
            multi_exitosa = False
            while not multi_exitosa:
                try:
                    cantidad = int(input("Ingrese la cantidad de numeros que desea mutliplicar: "))
                    for i in range(cantidad):
                        numero = int(input(f"Ingrese el {i+1}° numero: "))
                        resultado = resultado * numero
                    print(f"El resultado de la suma es: {resultado}")
                    multi_exitosa = True
                except ValueError:
                    print("Solo se permite el ingreso de numeros")
        case 4:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            try:
                resultado = num1 / num2
                print(f"El resultado de su division es: {resultado}")
            except ZeroDivisionError:
                print("No puede dividir por 0")
        case _:
            print("Opcion no valida, intente nuevamente")
    print("########Calculadora#########")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))   