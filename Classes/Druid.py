from Character import Character
from random import randint

class Druig(Character):
    def __init__(self, name, genre, age, hitdice):
        super().__init__(name, genre, age, hitdice)
        self._spells = []
        self._spellslots = {'Cantrips': 2,
                            'Level1': 2}

    def levelUp(self):
        super().levelUp()