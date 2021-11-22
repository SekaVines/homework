class Number:

    def __init__(self, my_number):
        self.my_number = my_number


    def bubble_sort(self, my_number):
        swapped = False
        for i in range(len(my_number) - 1, 0, -1):
            for j in range(i):
                if my_number[j] > my_number[j + 1]:
                    my_number[j], my_number[j + 1] = my_number[j + 1], my_number[j]
                    swapped = True
            if swapped:
                swapped = False
            else:
                break
        return my_number


print(f'Sorted list: {bubble_sort(self, my_number = [3, 4, 7, 67, 56, 87])}')


class Quicknumber:
    def __init__(self, my_list):
        self.my_list = my_list

    def quick_sort(self, my_list):
        if len(my_list) <= 1:
            return my_list

        a = my_list[0]
        b = list(filter(lambda num: num < a, my_list))
        c = [num for num in my_list if num == a]
        d = list(filter(lambda num: num > a, my_list))

        return quick_sort(b) + c + quick_sort(d)


print(f'Sorted list: {quick_sort(my_list=[9, 2, 4, 6, 78])}')
