print("Valor de bultos livianos: 1.000")
print("Valor de bultos mediano: 2.000")
bulto = int(input("Ingrese la cantidad de bultos a calcular: "))
peso_liviano = 0
peso_mediano = 0
for i in range(1,bulto+1):
    try:
        peso = int(input("Ingrese el peso del bulto: "))
        if peso <= 5:
            peso_liviano += 1
        elif peso <= 10:
            peso_mediano += 1
        else:
            print("Error, No hay informacion mas alla de 10 kilos")
    except ValueError:
        print("valor ingresado no es contable")
resultado_liviano = peso_liviano * 1000
resultado_mediano = peso_mediano * 2000

print(f"{peso_liviano} bultos livianos, total a pagar de bultos: {resultado_liviano}")
print(f"{peso_mediano} bultos medianos, total a pagar de bultos: {resultado_mediano}")


total = resultado_liviano + resultado_mediano
print(f"Total a pagar: {total}")