# lst = [1, 2, 3, 1, 4]
#
# set_1 = set()
# set_2 = set(lst)
#
# set_2.add(1)
#
# print(set_2)
# plov = {'рис', 'мясо', 'морковь'}
# beshbarmak = {'мясо', 'лапша', 'лук'}
#
# print(plov & beshbarmak)
# print(plov.intersection(beshbarmak))
#
# print(plov | beshbarmak)
# print(plov.union(beshbarmak))
#
# print(plov - beshbarmak)
# print(plov.difference(beshbarmak))
#
# print(plov ^ beshbarmak)
# print(plov.symmetric_difference(beshbarmak))
menu = {
    'plov': {'рис', 'мясо', 'морковь'},
    'beshbarmak': {'мясо', 'лапща', 'лук'},
    'kasha':{'крупа', 'молоко', 'сахар',}
}

quest = input('Choose: ')
for designation, ingridients in menu.items():
    if quest == designation:
        print(designation, ingridients)
    elif quest in ingridients:
        print(designation)
    else:
        print('good bay')







