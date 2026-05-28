diccionario = {"nombre" : "Cesar Huispe", 
               "fonos":[988778882,
                        988877776,
                        877666333],
    "activo": True
    }

#Busqueda
print("Nombre: ", diccionario["nombre"])
print("Fonos: ", diccionario["fonos"][1])
#Incsersion
diccionario["email"] = "cesar.huispe@example.com"
diccionario["fonos"].append(123456789)
print("Email:", diccionario["email"])
print("fono nuevo:", diccionario["fonos"][3])
#Actualizacion
diccionario["activo"] = False
diccionario["fonos"][0] = 99999999
#Eliminacion
del diccionario["activo"]
diccionario["fonos"].pop(2)

print(diccionario)