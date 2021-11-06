


# def auto_code(region):
#     while True:
#         a = input('введите код региона')
#         if  a == '01' or a =='1':
#             print('Бишкек')
#         elif a == '02' or a =='2':
#             print('Ош')
#         elif a == '03' or a =='3':
#              print('Баткенская область')
#         elif a == '04' or a =='4':
#              print('Джалал абадская область')
#         elif a == '05' or a =='5':
#              print('Нарынская область')
#         elif a == '06' or a =='6':
#              print('Ошская область')
#         elif a == '07' or a =='7':
#              print('Талаская область')
#         elif a == '07' or a =='8':
#              print('Чуйская область')
#         elif a == '09' or a =='9':
#             print('Иссык кульская область')
#         elif a == 'выйти' or a =='0':
#             print('вы вышли из системы')
#         else:
#             print('неверный код')
#
# auto_code('08')
# auto_code('7')
members = [
    {'name':'azat', 'age':18, 'heigt':185, 'physic':True},
    {'name': 'Adilet', 'age': 17, 'heigt': 180, 'physic':False},
    {'name': 'Asan', 'age': 20, 'heigt': 179, 'physic': True}

]

soldiers = []

def selection_army(member_lst: list):
    for member in member_lst:
        if member['age'] >= 18 and member['heigt'] >= 180 and member['physic'] == True:
            member['soldier'] = True
            soldiers.append(member_lst.pop(member))
    print(soldiers)

def add_member(name, age, heigt, physic):
    return {'name': name, 'age': age, 'heigt': heigt, 'physic': physic}

members.append(add_member('Ulan', 19, 181, True))
selection_army(members)

def find(name: str, lst: list):
    for member in lst:
        if member['name'] == name.title():
            return member
        print('не найден')

print(find('asan', members))

