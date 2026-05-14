edades= [23,54,12,8,86,8,-1,98]
i = 0
menor_edad = 0
mayor_edad = 0
while i < len(edades) and edades[i] != -1:
    if edades[i] >= 18:
        mayor_edad += 1
    elif edades[i] < 18:
        menor_edad += 1