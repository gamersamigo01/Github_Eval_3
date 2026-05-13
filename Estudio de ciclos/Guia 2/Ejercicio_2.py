notas = [2.5,6.7,5.5,7.0,4.2]
suma = 0

for i in notas:
    suma = i + suma
promedio = suma / (len(notas))
print("Su promedio:",promedio)

if promedio >= 4.0:
    print("Aprueba")
elif promedio >= 3.0:
    print("Habilita")
else:
    print("Reprueba")