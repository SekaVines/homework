vowles = 'a', 'e', 'i', 'y', 'o', 'u'
consonant = 'q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
vowles_list = []
consonant_list = []

print(len(vowles))
count = 0
while len(vowles_list) != 5:
    count += 1
    word = input('Введите слово').lower()
    for letter in word:
        if letter in vowles:
            vowles_list.append(letter)
        elif letter in consonant:
            consonant_list.append(letter)
    if len(vowles_list) == 5:
        break
print(vowles_list)
print(consonant_list)




# tpl = tuple()
# tpl1 = ()
#
# numbers = (1, 2, 3, 4, 5)
# text = ('abc', 'efg')
# print(id(numbers))
#
# numbers = numbers + text
# print(numbers)
# print(id(numbers))
#
#
#
# numbers = list(numbers)
# print(type(numbers))
# numbers.append(5)
# print(numbers)
