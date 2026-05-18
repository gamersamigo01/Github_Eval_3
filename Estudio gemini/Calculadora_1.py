print("########Calculadora#########")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
opcion = int(input("Ingrese una opcion: "))
resultado = 0

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
                    print("Solo se permite el ingres de numeros")
        case 2:
            suma_exitosa = False
            while not suma_exitosa:
                try:
                    cantidad = int(input("Ingrese la cantidad de numeros que desea restar: "))
                    for i in range(cantidad):
                        numero = int(input(f"Ingrese el {i+1}° numero: "))
                        resultado = numero - resultado
                    print(f"El resultado de la resta es: {resultado}")
                    suma_exitosa = True
                except ValueError:
                    print("Solo se permite el ingresar de numeros")
        case 3:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            resultado = num1 * num2
            print(f"El resultado de su multiplicacion es: {resultado}")
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