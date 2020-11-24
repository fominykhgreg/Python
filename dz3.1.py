def delenie(x, y):
    while True:
        if y == 0:
            print("Нельзя делить на ноль.")
            y=int(input("Введите второе число:"))
        else:
            return x / y


x = int(input("Введите перове число:"))
y = int(input("Введите второе число:"))
print("Результат:", round(delenie(x, y), 3))
