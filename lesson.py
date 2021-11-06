names = ('one', 'two', 'three', 'four')
numbers = 1, 2, 3, 4

# for i in range(1, 4):
#  numbers.append(i)

dict_3 = dict(zip(numbers, names))


if 3 in dict_3:
    print(dict_3[3])

# print(names)
# print(numbers)
# print(dict_3)
#
dict_4 = dict([(2, 'ghbmhnj'), (9, 'hfmgvbn'), (names, 'three')])
# print(dict_4)
a = {**dict_3, **dict_4}
print(a)
# dict_1 = {
#     'def' : 1,
#     'if' : 2,
#     'three': 3,
#     'four': 4,
#     'numbers': [1,2,3],
#     'names': names,
# }

# dict_1 = ['navts','numbers']
#
# del dict_1 ['navts']
# dict_1.pop('numbers')
#
# print(dict_1)
# student = ( gfyhk)
#
# dict_1['five'] = 5
#
# dict_1['def'] = 'definition'
# dict_1['if'] = 'condition'
#
# print(dict_1)
#
# # dict_1.update(student)
# dict_1 = (**student, **dict_1)
# print(dict_1)








