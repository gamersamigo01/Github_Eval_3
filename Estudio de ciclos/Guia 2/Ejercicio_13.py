clave_correcta = "Python123"
clave_intento = ["Hola","123", "Python123"]
i = 0
acceso = True
while i < 3 and i < len(clave_intento): #i por si solo es el contador, y el i < len(Clave_intento) sirve para que el contador sea menor al total de palabras puestas
    if clave_intento[i] != clave_correcta:
        i += 1
        print("Clave incorrecta")
        acceso = False
        
    else:
        print("Clave correcta")
        acceso = True
        break
print(f"¿Tiene acceso?: {acceso}")