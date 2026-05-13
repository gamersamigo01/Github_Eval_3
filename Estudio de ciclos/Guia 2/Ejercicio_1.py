for i in range(1,21):
    if i % 2 == 0:
        print(f"Su numero {i} es par")
        if i % 5 == 0:
            print(f"Su numero {i} es par y multiplo de 5")
    elif i % 2 != 0:
        print(f"Su numero {i} es impar")
        if i % 5 == 0:
            print(f"Su numero {i} es impar y multiplo de 5")    