
while True:
    vvod = input("Элементы списка(через пробел):").split()

    if len(vvod)<2:
        print("Введите более одного знаечния")

    else:
        mas1=[]
        mas2=[]
        newVvod=[]
        print(vvod)
        i=0
        while i<len(vvod):
            if i%2==0:
               mas1.append(vvod[i])
            else:
               mas2.append(vvod[i])
            i += 1

        j=0
        while j<len(vvod):
            newVvod.append(mas2[j])
            newVvod.append(mas1[j])
            j += 1
            if len(mas2)==j:
                if (len(mas1)+len(mas2))%2!=0:
                    newVvod.append(vvod[-1])
                break
            if len(mas1)==j:
                break

        print(newVvod)
