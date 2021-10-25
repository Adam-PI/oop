class Parentse:
    def __init__(self, name="Я", age=1, haircolor="черный"):
        self.age = age
        self.name = name
        self.haircolor = haircolor


class Son(Parentse):
    def push_ups(self):
        print("Делаю отжимания")


class Daughter(Parentse):

    def abs(self):
        print("качаю пресс")


class NevedomayaIgrushka(Parentse):
    def song(self):
        print("пою когда нажимают кнопку на моем животе")


Usman = Son("Усман", 45, "коричневый")
Usman.push_ups()

Kamila = Daughter("Камила", 19, "блонд")
Kamila.abs()

Dino = NevedomayaIgrushka("Дино", 0, "нету")
Dino.song()

print("изменение")