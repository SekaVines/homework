def plus(H, l):
    return float(H*l)
square = plus(20, 4)
print(square)

def plus(*args):
    return int(sum(args))/len(args)
print(plus(2,3,5,6,7))

def menu(bite,lunch,dinner):
    return {'завтрак': bite, 'обед': lunch, 'ужин': dinner}
dinner = menu("soup", "rice", "manti")
bite = menu("egg","kasha","coffe")
lunch = menu("plof","lagman","oromo")
print(dinner)
print(bite)
print(lunch)