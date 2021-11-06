list1 = [5, 2.5, 1, 8, 3, 6, 4]
odds = []
evens = []

for i in list1:
    if i % 2 == 0:
        evens.append(i)
    elif i % 2 != 0:
        odds.append(i)

print(sorted(odds))
print(sorted(evens))