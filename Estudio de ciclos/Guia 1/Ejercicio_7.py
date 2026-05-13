try: 
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    resultado = num1 //  num2
except ZeroDivisionError:
    print("No puede dividir por 0")
    num2 = int(input("Ingrese el segundo numero nuevamente: "))

resultado = num1 //  num2

print(f"El resultado de su division es: {resultado}")
print("fin del programa")