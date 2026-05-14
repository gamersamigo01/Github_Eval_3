num = [-2, 34,0,0,-250, 123,1]
negativo = 0
positivo = 0
ceros = 0
for numero in num:
    if numero < 0:
        negativo += 1
    elif numero == 0:
        ceros += 1
    else: 
        positivo += 1

print(f"Su lista tiene {positivo} numeros positivos")
print(f"Su lista tiene {negativo} numeros negatvios")
print(f"Su lista tiene {ceros} ceros")