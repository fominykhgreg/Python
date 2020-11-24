def summaChisel():
    summa = []
    while True:
        chisla = input("Введите числа через пробел:").split()
        for el in chisla:
            if el =="q":
                print(sum(summa))
                return
            summa.append(int(el))
        print(sum(summa))

summaChisel()