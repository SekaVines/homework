class Car:
    def __init__(self, brand, color, type_car, amount_passenger, max_speed, engine, county, year, mechanic):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string!')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(type_car, str):
            self.type_car = type_car
        else:
            raise ValueError('type_car should be string')
        if isinstance(amount_passenger, int):
            self.amount_passenger = amount_passenger
        else:
            raise ValueError('amount_passenger should be string')
        if isinstance(max_speed, int):
            self.max_speed = max_speed
        else:
            raise ValueError('max_speed should be string')
        if isinstance(engine, float):
            self.engine = engine
        else:
            raise ValueError('engine should be float')
        if isinstance(county, str):
            self.country = county
        else:
            raise ValueError('country should be string')
        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError('year should be int')
        if isinstance(mechanic, str):
            self.mechanic = mechanic
        else:
            raise ValueError('mechanic should be str')

    def tunning(self, cost):
        car_cost = 1000
        summary = car_cost + cost
        return summary
    def __str__(self):
        return f'{self.brand}, {self.color}, {self.engine}, {self.year}, {self.country}, {self.mechanic}, {self.max_speed}, {self.amount_passenger}, {self.type_car}'



car1 = Car(brand='BMW', color='black', year=2021, county='Germany', amount_passenger=4, max_speed=360, type_car='Crossower', engine=6.0, mechanic='Nope')
print(car1)
print(car1.tunning(8000000000))