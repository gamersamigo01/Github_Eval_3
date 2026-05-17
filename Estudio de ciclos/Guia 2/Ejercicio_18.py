i = 16
while i  >= 0:
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: TicTac")
    elif i % 3== 0:
        print(f"{i}: Tic")
    elif i % 5 == 0:
        print(f"{i}: tac")
    else:
        print(i)
    i -= 1