class TownCar:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police
    def go(self):
        print('auto going')

    def stop(self):
        print('auto stoing')

    def trun(self):
        print('auto truning')

class SportCar(TownCar):
    pass

class WorkCar(TownCar):
    pass

class PoliceCar(TownCar):
    pass

sportCar = SportCar(240, 'red', 'Ferarri')

for i in SportCar:
    print(i)