from Character import Character
from random import randint

class Fighter(Character):
    def __init__(self, name, genre, age, hitdice):
        super().__init__(name, genre, age, hitdice)

    def levelUp(self):
        super().levelUp()