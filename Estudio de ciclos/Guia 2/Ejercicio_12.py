entradas = [3,6,19,20,-23,-2,0,45]
suma = 0
Positivos = 0
negativos = 0
i = 0
while entradas[i] != 0 and i < len(entradas): 
    if entradas[i] > 0:
        Positivos += 1
    elif entradas[i] < 0:
        negativos += 1

    suma += entradas[i]
    i += 1

print(f"Suma: {suma}")
print(f"Positivos: {Positivos}")
print(f"Negativo: {negativos}")    
    