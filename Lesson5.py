def plus(a, *args):
    return a + sum(args)
print(plus(5,5))

def dct(**kwargs):
    print(kwargs)

dct(a=1, b=2, c=3)















def menu(breakfast, lunch, dinner='торт'):
    return {' завтрак': breakfast, 'обед': lunch, 'ужин': dinner}

def show(dict1: dict):
    for i, k in dict1.items():
        print(i, '-', k)

monday = menu("каша", "суп", "плов")
tuesday = menu('манты', "яичница", "бананы")
friday = menu('чай', 'борщ')
# show(monday)
# show(menu(dinner="торт", breakfast="сок", lunch="омлет"))
# print(monday)
# print(tuesday)
# print(friday)
















