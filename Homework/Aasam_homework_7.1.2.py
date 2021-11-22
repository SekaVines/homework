class Palindrome:
    def __init__(self, number: int):
        if isinstance(number, int):
            self.num = number
        else:
            raise ValueError('Полиндром целое число')
        self.evenly = False

    def palindrome_(self):
        if self.num <= 0:
            return False
        a = len(str(self.num)) - 1
        for i in range(len(str(self.num))):
            if self.num // 10 ** i % 10 != self.num // 10 ** a % 10:
                return False
            a -= 1
        return True


number_1 = Palindrome(number=343)
print(f'If {number_1.num} is a palindrome: {number_1.palindrome_()} (Math method)')