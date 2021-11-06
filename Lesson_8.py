import time

with open('results.txt', 'r') as gmn:
    for line in gmn:
        for i in line:
            print(i, end='')
            time.sleep(0.1)







# from pprint import pprint
#
# with open('file.txt', 'w') as file:
#     file.write('My names is johny \n')
#
# with open('file.txt', 'a') as file:
#     file.write('I am from USA \n')
#
# with open('file.txt', 'r') as file:
#     pprint(file.read())


