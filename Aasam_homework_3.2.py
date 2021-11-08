class Feline:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def the_norm_weight(self):
        return f'the norm: {self.weight} they can be very different'

    def the_norm_height(self):
        return f'the norm: {self.height} they can be very different'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Weight: {self.weight}\n' \
               f'Height: {self.height}'


feline_1 = Feline(name='feline',
                  age=2,
                  weight=200,
                  height=70)
print(feline_1)
print(feline_1.the_norm_height())
print(feline_1.the_norm_weight())


class Tiger(Feline):
    def __init__(self, name, age, weight, height, colour):
        super().__init__(name, age, weight, height)
        self.colour = colour

    def the_norm_height_tiger(self):
        return f'the norm: {self.height} almost 300cm'

    def the_norm_weigh_tiger(self):
        return f'the norm: {self.weight} almost 190kg'

    def __str__(self):
        return super(Tiger, self).__str__() + f'\nColour : {self.colour}'


tiger_1 = Tiger(name='Tiger',
                age=2,
                weight=190,
                height=300,
                colour='black and orange')
print(tiger_1)


class Lion(Feline):
    def __init__(self, name, age, weight, height, power):
        super().__init__(name, age, weight, height)
        self.power = power

    def the_norm_height_lion(self):
        return f'the norm: {self.height} almost 250cm'

    def the_norm_weigh_tiger(self):
        return f'the norm: {self.weight} almost 250kg'

    def __str__(self):
        return super(Lion, self).__str__() + f'\nPower : {self.power}'


lion_1 = Lion(name='Lion',
              age=3,
              weight=250,
              height=250,
              power='stark')
print(lion_1)


class Ligr(Tiger, Lion):
    def __init__(self, name, age, weight, height, colour, about):
        super().__init__(name, age, weight, height, colour)
        self.about = about

    def the_norm_height_ligr(self):
        return f'the norm: {self.height} almost 400cm'

    def the_norm_weigh_ligr(self):
        return f'the norm: {self.weight} almost 450kg'

    def __str__(self):
        return super(Ligr, self).__str__() + f'\nAbout : {self.about}'


ligr_1 = Ligr(name='ligr',
              age=3,
              weight=450,
              height=400,
              colour='yellow',
              about='big')
print(ligr_1)


class Ufcfighter:
    def __init__(self, name, age, weight_category, style):
        self.name = name
        self.age = age
        self.weight_category = weight_category
        self.style = style

    def year(self):
        return f'restriction on {self.age}'

    def techniques(self):
        return f'some techniques are prohibited'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Weight_category: {self.weight_category}\n' \
               f'Style: {self.style}'


class Wrestlers(Ufcfighter):
    def __init__(self, name, age, weight_category, style):
        super().__init__(name, age, weight_category, style)

    def year_wrestlers(self):
        return f'restriction on {self.age}'

    def techniques_wrestlers(self):
        return f'some techniques are prohibited'

    def __str__(self):
        return super(Wrestlers, self).__str__()


wrestlers_1 = Wrestlers(name='Khabib Nurmagamedov',
                        age=32,
                        weight_category='light weight',
                        style='wrestler')
print(wrestlers_1)


class Cutters(Ufcfighter):
    def __init__(self, name, age, weight_category, style):
        super().__init__(name, age, weight_category, style)

    def year_cutters(self):
        return f'restriction on {self.age}'

    def techniques_cutters(self):
        return f'some techniques are prohibited'

    def __str__(self):
        return super(Cutters, self).__str__()


cutters_1 = Cutters(name='Conor Mcgregor',
                    age=35,
                    weight_category='light weight',
                    style='cutters')


class Universal(Ufcfighter):
    def __init__(self, name, age, weight_category, style):
        super().__init__(name, age, weight_category, style)

    def year_universal(self):
        return f'restriction on {self.age}'

    def techniques_universal(self):
        return f'some techniques are prohibited'

    def __str__(self):
        return super(Universal, self).__str__()


universal_1 = Universal(name='Kamaru Usman',
                        age=32,
                        weight_category='welterweight',
                        style='universal')
print(universal_1)
