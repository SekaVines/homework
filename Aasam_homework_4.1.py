def data(day, month, name = 'user'):
    if day > 31 or month > 12 or type(name) != str:
        return "ERROR !"

    if (day >= 21 and month == 3) or (day <= 19 and month == 4):
        return name, 'Овен'
    elif day >= 20 and month == 4 or day <= 20 and month == 5:
        return name, 'Телец'
    elif day >= 21 and month == 5 or day <=20 and month == 6:
        return name, 'Близнецы'
    elif day >= 21 and month == 6 or day <=22 and month == 7:
        return name, 'Рак'
    elif day >= 23 and month == 7 or day <=22 and month == 8:
        return name, 'Лев'
    elif day >= 23 and month == 8 or day <=22 and month == 9:
        return name, 'Дева'
    elif day >= 23 and month == 9 or day <=22 and month == 10:
        return name, 'Весы'
    elif day >= 23 and month == 10 or day <=21 and month == 11:
        return name, 'Скорпион'
    elif day >= 22 and month == 11 or day <=21 and month == 12:
        return name, 'Стрелец'
    elif day >= 22 and month == 12 or day <=20 and month == 1:
        return name, 'Козерог'
    elif day >= 21 and month == 1 or day <=18 and month == 2:
        return name, 'Водолей'
    elif day >= 19 and month == 2 or day <=20 and month == 3:
        return name, 'Рыбы'
person = data(12, 3, 'lola')
print(person)
