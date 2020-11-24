def my_func(x, y, z):
    if y > x < z:
        j1 = 0
    else:
        j1 = x

    if x > y < z:
        j2 = 0
    else:
        j2 = y

    if x > z < y:
        j3 = 0
    else:
        j3 = z
    return j1 + j2 + j3


result = my_func(x=int(input("Первое число:")), y=int(input("Второе число:")), z=int(input("Третье число:")))

print(f"Сумма максимальных двух чисел будет равна:{result}")
