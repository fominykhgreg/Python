ch = int(input("Введи число:"))
stroka = str(ch)

i = 0
max = 0

while i < len(stroka):
    if int(stroka[i]) == 9:
        max = 9
        break
    if int(stroka[i])>max:
        max = int(stroka[i])
    i += 1


print(max)