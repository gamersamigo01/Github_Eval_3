for i in range(2,31):
    es_primo = True

    for divisor in range(2,i):
        if i % divisor == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"{i}: es primo")
    else:
        print(f"{i}: no es primo")