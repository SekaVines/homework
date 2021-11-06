import random
from random import choice
from datetime import datetime
import time
# start = datetime.now()
#
# time.sleep(5)
# end = datetime.now() - start
# print(end)
#
# c = 0
# def timer(num):
#     while num != 0:
#         num -= 1
#         time.sleep(1)
#         print(num)
# timer(3)
student = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

while len(student) != 0:
    q = input('Пролдолжать у/n')
    if q == 'y'.lower():
        # number = random.choice(student)
        print(student.pop(student.index(random.choice(student))))
        # student.remove(number)
        print(student)
    elif q == 'n'.lower():
        print('Программа завершена')
        break








# from random import randint, choice, randrange, sample
#
# print(randint(5, 10))
#
# tpl = 1, 2, 3, 4, 5
# print(choice(tpl))
#
# print(sample(tpl, 2))
#
# print(randrange(1, 10, 2))
