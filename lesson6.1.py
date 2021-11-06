names = ['adil', 'samat', 'erkin', 'max', 'azamat', 'abdrachim' ]

filter_names = list(filter(lambda word: word.startswith('a'), names))

def index_list(lst):
    while True:
        try:
            position = int(input('Введите индекс'))
            print(lst[position])
        except IndexError:
            print(f'Вводите от 0 до {len(lst)-1} ')
        except:
            print('Вы ввели совсем не то !')

index_list(filter_names)

