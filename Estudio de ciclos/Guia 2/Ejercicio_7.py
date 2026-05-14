for i in range(2,31): #Se recorre la lista completa hasta 30
    es_primo = True

    for divisor in range(2,i): #Aca se recorren todos los numeros antes de i, por ejemplo si i es 5, recorre 2,3,4 y los divide 5./
                               #si alguno de estos da == 0, significan que no son primos pues se puede dividir por otro numero que no sea 5 y 1
        if i % divisor == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"{i}: es primo")
    else:
        print(f"{i}: no es primo")