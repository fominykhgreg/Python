list = [7, 5, 3, 3, 2]
print(list)
i=0
while True:

    new = int(input("Введите число:"))

    if new >=max(list):
        list.insert(0,new)
        print(list)
    elif new<=min(list):
        list.append(new)
        print(list)

    else:
        while i<len(list):
            if new >=list[i]:
                list.insert(i,new)
                i+=1
                print(list)
                i=0
                break
            else:
                i+=1

#print(list)





