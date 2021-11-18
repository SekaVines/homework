class Sumnumbers:
    def __init__(self, numbers: list, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def index_numbers(self):
        for index in range(len(self.numbers)):
            for inner_index in range(index + 1, len(self.numbers)):
                if (self.numbers[index] + self.numbers[inner_index]) == self.desired_sum:
                    return [index, inner_index]
        return None

    def __str__(self):
        return f'List of numbers: {self.numbers}\n' \
               f'Desired number: {self.desired_sum}\n'


number = Sumnumbers(numbers=[7, 2, 11, 15], desired_sum=9)
print(number)
print(number.index_numbers())
