my_list = [3, 1, 81, 35, 22]


def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list


    a = my_list[0]
    b = list(filter(lambda num: num < a, my_list))
    c = [num for num in my_list if num == a]
    d = list(filter(lambda num: num > a, my_list))

    return quick_sort(b) + c + quick_sort(d)


print(f'Sorted list: {quick_sort(my_list)}')
