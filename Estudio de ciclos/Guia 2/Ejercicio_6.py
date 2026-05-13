edad = [5,34,14,72,61,10]

for i in edad:
    if i > 0 and i < 12:
        print(f"{i}: Es un niño")
    elif i >= 12 and i < 18:
        print(f"{i}: Es un adolecente")
    elif i >= 18 and i < 60:
        print(f"{i}: Es adulto")
    elif i >= 60:
        print(f"{i}: Es adulto mayor")