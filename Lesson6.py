from random import randint

print(randint(1, 23))





# a = lambda a, b: a + b
# print(a(2, 3))
# print(type(a))
# print(10 + (lambda x: x ** 2)(2))
#
# b = (lambda x, y=2: x + y)(4, 6)
# print(b)
# print(type(b))

# words = ['kg', 'kz', 'ru', 'ua', 'gb']
# names = ['adil', 'samat', 'erkin', 'max', 'azamat', 'abdrachim' ]

# def up_l(word):
#     return word.upper()
#
# def edit_f(lst, func):
#     for word in lst:
#         print(func(word))

# edit(words, up_l)
# edit_f(names, up_l)

# edit_l = list(map(lambda word: word.upper(), words))
# print(edit_l)
# print(list(map(lambda word: word.upper(), names)))
#
# filter_names = list(filter(lambda word: not word.startswith('a') and len(word) > 5, names))
#
# print(filter_names)