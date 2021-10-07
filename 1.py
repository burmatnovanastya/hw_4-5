name = input('Введите имя')
surname = input('Введите фамилию')
year = int(input('Введите год рождения'))
print(name, '_', surname, '_', year)
name, surname = surname, name
year += 60
print(name, '_', surname, '_', year)
