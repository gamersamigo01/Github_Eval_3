pasajes = int(input("¡Cuantos pasajes va a vender?: "))

totalingresos = 0

for i in range(pasajes+1):
    try:
        costo = int(input("Ingrese el coste del pasaje: "))
        totalingresos = costo + totalingresos
    except ValueError:
            print("Error, Tiene que ser un digito")
            
print(f"El total de las ventas de los pasajes es de: {totalingresos}")