class Tarif:
    def __init__(self, number, name, summary,):
        self.number = number
        self.name = name
        self.summary = summary

    def call(self):
        return f'This number: {self.number}, can call but with restriction'

    def __str__(self):
        return f'Name: {self.name}\n' \
                f'Number: {self.number}\n' \
                f'Summary: {self.summary}'

number_1 = Tarif(name='Adilet', number='0502960697', summary='120')

class UnlCallTarif(Tarif):
    def unl_call(self):
        return f'This number: {self.number}, can call but without restriction'

    def __str__(self):
        return super(UnlCallTarif, self).__str__()
number_2 = UnlCallTarif(name='Ailin', number='0552667765', summary='1500')

class UnlInternetTarif(Tarif):
    def unl_internet(self):
        return f'Your Internet package is unlimited'
    def __str__(self):
        return super(UnlInternetTarif, self).__str__()
number_3 = UnlInternetTarif(name='Georg',
                            number='0777-777-777',
                            summary=4000)

class DiamondTarif(UnlInternetTarif, UnlCallTarif):


    def __str__(self):
        return super(DiamondTarif, self).__str__()

dimond = DiamondTarif(name='Aasam',
                      number='0999-999-999',
                      summary=9999)

print(dimond.unl_call())
print(dimond.unl_internet())
print(dimond)