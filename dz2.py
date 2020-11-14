second = int(input("введите время в секундах:"))

hour = int(second//3600)
min = (second %3600)//60
sec = (second%60)%60

print(hour,min,sec)
print(f'{hour:02}:{min:02}:{sec:02}')