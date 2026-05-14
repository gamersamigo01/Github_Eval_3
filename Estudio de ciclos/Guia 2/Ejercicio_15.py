num = 0
sum = 1
while num <= 100:
    if num % 2 == 0:
        print(f"{num}, es par")
    else:
        print(f"{num}, es impar")
    
    siguiente = num + sum # suma num = 0, mas sum = 1 entonce siguiente = 1
    num = sum # num se transforma a sum o sea num =1
    sum = siguiente # sum se transforma en la suma o sea = 1
    