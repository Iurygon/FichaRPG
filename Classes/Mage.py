from  Character import Character
from random import randint

class Mage(Character):
    def __init__(self, name, genre, age):
        super().__init__(name, genre, age)
        self._hp = randint(1, 6) + round(self._constitution/2)
        self._mp = randint(1, 10) + round(self._intelligence/2)
        pass

    def levelUp(self):
        super().levelUp()
        self._hp += randint(1, 6)
        self._mp += randint(1, 10)
