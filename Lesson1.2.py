class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_calcute(self, number_1, number_2):
        summary = number_1 + number_2
        return summary

    def can_say_hello(self):
        return 'Hello World'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}'


class Programmer(Human):
    def __init__(self, name, age, language, fast_typing, logic):
        super().__init__(self, name)
        self.language = language
        self.fast_typing = fast_typing
        self.logic = logic

    def can_feeely_use_laptop(self):
        print('dfgfhghjk')

    def __str__(self):
        return f'languages {self.language}\n' \
               f'Fast Typing {self.fast_typing}\n' \
               f'Logic: {self.logic}'


human_1 = Human(name='Aasam', age=24)
print(human_1.can_calcute(int(input('First:')), int(input('Two:'))))
print(human_1)
proger = Programmer(language='Pytoh',
                    fast_typing='True', logic='True',
                    name='Aa', age=25)
print(proger)
