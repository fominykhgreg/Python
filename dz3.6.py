def int_func(*x):
    i = 0
    summa = []
    gotov = []

    while i < len(x):
        summa.append(str(x[i]).title())
        i += 1
    j = 0
    while j < len(summa):
        gotov = "" + str(summa[j])
        j += 1

    return gotov


print(int_func("случайный текст маленькими буквами"))
