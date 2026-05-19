correos = ["Luciano.gomez","Javieraraneda@pan","Tomasgonzales@gmail.com"]
i = 0
correcto = False
while i < len(correos) and not correcto:
    correo = correos[i]
    poscision_arroba = correo.find("@")
    poscicion_punto = correo.rfind(".")
    
    if poscision_arroba > 0 and poscicion_punto > poscision_arroba +1:
        correcto = True
        print("Correo --> Valido")
    else:
        print("Correo ---> Invalido")
    i += 1
        