data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters_list = []
numbers_list = []

for i in data_tuple:
    if type(i) == str:
        letters_list.append(i)
    if type(i) == int:
        numbers_list.append(i)
    if type(i) == float:
        numbers_list.append(i)
    if type(i) == bool:
        numbers_list.append(i)
numbers_list.remove(6.13)
letters_list.append(numbers_list.pop(0))
numbers_list.insert(1,2)
letters_list.reverse()
letters_list[1] = 'G'
letters_list[7] = 'c'

print(letters_list)
print(sorted(numbers_list))