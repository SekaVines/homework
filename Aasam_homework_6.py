five_list = (1, 2, 3, 4, 5)

ten_list = list(map(lambda x: x+5, five_list))

ten_list.extend(five_list)
sorted(ten_list)

ten_list = list(filter(lambda a: a%2 == 0, ten_list))

def index_list(lst):
    while True:
        try:
            a = int(input('Введите индекс'))
            print(lst[a])
        except IndexError:
            print(f'Вводите от 0 до {len(lst)-1}')
        except:
            print('Вы ввели совсем не то !')
        break

index_list(ten_list)