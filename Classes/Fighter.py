from Character import Character
from random import randint

class Fighter(Character):
    def __init__(self, name, genre, age):
        super().__init__(name, genre, age)
        self._hp = randint(1, 10) + round(self._constitution/2)

    def levelUp(self):
        super().levelUp()
        self._hp += randint(1, 10) + round(self._constitution/2)