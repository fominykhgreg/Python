chislo = int(input("Введите число от 1 до 12:"))
while chislo > 12:
    print("Введите корректное значение.")
    chislo = int(input("Введите число от 1 до 12:"))
a= [1,2,3,4,5,6,7,8,9,10,11,12]
b=["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]

i=0
while i < len(a):
    if chislo==a[i]:
        print(f'{"Время года: "}{b[i]}')
        i+=1
    else:
        i+=1



