frase = "Hola chaval"
vocales = "aeiou"
num_vocales = 0
num_consonantes = 0
num_espacios = 0
for i in frase:
    if i in vocales:
        num_vocales += 1
    elif i == " ":
        num_espacios += 1
    elif i.isalpha():
        num_consonantes += 1
print(f"Su frase tiene {num_vocales} vocales")
print(f"Su frase tiene {num_espacios} espacios")
print(f"Su frase tiene {num_consonantes} consonantes")