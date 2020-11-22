def data(name, lastname, year, city, email, phone):
    return (
        f"Имя-{name.title()} Фамилия-{lastname.title()} Год рождения-{year} Город проживания-{city.title()} Адрес электронной почты-{email} Телефон-{phone}")


print(data(name=input("Введите имя:"), lastname=input("Введите фамилию:"), year=input("Введите год рождения:"),
           city=input("Введите город проживания:"), email=input("Введите электронную почту:"),
           phone=input("Введите телефон:")))
