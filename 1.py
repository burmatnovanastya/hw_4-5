name = input()
surname = input()
year = int(input())
print(name, '_', surname, '_', year)
name, surname = surname, name
year += 60
print(name, '_', surname, '_', year)
