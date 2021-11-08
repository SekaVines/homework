class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n'


child_1 = Child(name='Azat',
                age=12)
print(child_1)


class Father(Child):
    def __init__(self, name, age, experience, understanding):
        super().__init__(name, age)
        self.experience = experience
        self.understanding = understanding

    def __str__(self):
        return super(Father, self).__str__() + f'\nExperience : {self.experience}\n' \
                                               f'Understandig : {self.understanding}'


father_1 = Father(name='Azamat',
                  age=45,
                  experience='have',
                  understanding='understanding about life')
print(father_1)


class Grandfather(Father):
    def __init__(self, name, age, experience, understanding, knows_much, condition):
        super().__init__(name, age, experience, understanding)
        self.knows_much = knows_much
        self.condition = condition

    def __str__(self):
        return super(Grandfather, self).__str__() + f'\nKnows_much : {self.knows_much}\n' \
                                                    f'Condition : {self.condition}'


Grandfather_1 = Grandfather(name='Zhumaly',
                            age=100,
                            experience='have',
                            understanding='the meaning of life',
                            knows_much='knows about life',
                            condition='old')
print(Grandfather_1)


class Account:
    def __init__(self, name, age, email, password, data):
        self.__data = None
        self.__data = data
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.data = data

    def _information(self):
        return f'Protected {self.password}'

    def __data(self):
        return f'Protected {self.data}'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Email: {self.email}\n' \
               f'Password: {self.password}\n' \
               f'Data: {self.data}'


account_1 = Account(name='Aazam',
                    age=15,
                    email='aazam@gmail.com',
                    password=3456789,
                    data='data')


# print(account_1)
# print(account_1.__data)
# print(account_1._information)


class Soldat:
    def __init__(self, name, age, attack):
        self.name = name
        self.age = age
        self.attack = attack

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Attack: {self.attack}\n'


class Sniper(Soldat):
    def __init__(self, name, age, attack):
        super().__init__(name, age, attack)

    def __str__(self):
        return super(Sniper, self).__str__()


sniper_1 = Sniper(name='sniper',
                  age=24,
                  attack='Стреляет с снайпера')
print(sniper_1)


class Para(Soldat):
    def __init__(self, name, age, attack):
        super().__init__(name, age, attack)

    def __str__(self):
        return super(Para, self).__str__()


para_1 = Para(name='para',
              age=20,
              attack='стреляет с AKC-74')
print(para_1)


class Pilot(Soldat):
    def __init__(self, name, age, attack):
        super().__init__(name, age, attack)

    def __str__(self):
        return super(Pilot, self).__str__()


pilot_1 = Pilot(name='pilot',
                age=29,
                attack='Атакует с помощью самолёта')
print(pilot_1)


class English:
    def declarations_of_love(self):
        print("I Love You")


class German:
    def declarations_of_love(self):
        print("Ich liebe dir")


class Russian:
    def declarations_of_love(self):
        print("Я люблю тебя")


def intro(language):
    language.declarations_of_love()


a = English()
print(a)
b = German()
print(b)
c = Russian()
print(c)