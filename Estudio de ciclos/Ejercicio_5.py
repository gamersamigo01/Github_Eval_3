numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

resultado = 0
try:
    resultado = numero1 // numero2
except ZeroDivisionError:
    while numero2 == 0:
        print("No se puede dividir por 0")
        numero2 = int(input("Ingrese el segundo numero nuevamente: "))
    resultado = numero1 // numero2

print(f"El resultado de su division es: {resultado}")