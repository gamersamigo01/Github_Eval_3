sacar = [2000,5000,10000,1000]
saldo = 20_000
i = 0

while i < len(sacar): #ocupar esto en varios while
    retiro = sacar[i] #Esto sirve para sacar cada valor de la lista, sacar[1] se refiere a la poscicion en la lista, y el retiro toma lo que hay en esa poscicion
    if retiro <= 0:
        print("Error, tiene que retirar mas de 0")
    elif retiro > 0:
        saldo -= retiro
        print(f"Retiro exitoso: {retiro}, le queda: {saldo} de saldo")
    else:
        print(f"Fondos insuficientes para retirar {retiro}")

    i += 1