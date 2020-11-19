slova = input("Введите слова:").split()

print(slova)
i=0
while i<len(slova):
    print(f'{i+1}:{(slova[i])[:10].title()}')
    i+=1