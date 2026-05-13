for i in range(1,51):
    divisible_3 = i % 3 == 0
    divisible_7 = i % 7 == 0
    if (divisible_3 or divisible_7) and not (divisible_3 and divisible_7):
        print(i)