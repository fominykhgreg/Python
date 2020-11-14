vyruchka = int(input("Ведите сумму выручки:"))
izderjki = int(input("Ведите сумму издержек:"))

pribyl = (vyruchka - izderjki)
rentabelnost = pribyl/vyruchka

if vyruchka > izderjki :
    print("Фирма приносит прибыль")
    print("Рентабельность фирмы:",round(rentabelnost,3))

else:
    print("Фирма приносит убыток")

chislennost = int(input("Введите численность сотрудников:"))

print("Прибыль фирмы в расчете на одного сотрудника:",round(pribyl/chislennost,2))