from Character import Character
from random import randint

class Mage(Character):
    def __init__(self, name, genre, age):
        super().__init__(name, genre, age)
        self._hp         = randint(1, 6) + round(self._constitution/2)
        self._grimoire   = []
        self._spellslots = {'Tricks': 3,
                            'Level1:': 2}

    def levelUp(self):
        super().levelUp()
        self._hp += randint(1, 6) + round(self._constitution/2)
        if self._level == 1:
            self._spellslots = {'Tricks': 3,
                                'Level1:': 2}
        elif self._level == 2:
            self._spellslots = {'Tricks': 3,
                                'Level1': 3}
        elif self._level == 3:
            self._spellslots = {'Tricks': 3,
                                'Level1': 4,
                                'Level2': 2}
        elif self._level == 4:
            self._spellslots = {'Tricks': 4,
                                'Level1': 4,
                                'Level2': 3}
        elif self._level == 5:
            self._spellslots = {'Tricks': 4,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 2}
        elif self._level == 6:
            self._spellslots = {'Tricks': 4,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3}
        elif self._level == 7:
            self._spellslots = {'Tricks': 4,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 1}
        elif self._level == 8:
            self._spellslots = {'Tricks': 4,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 2}
        elif self._level == 9:
            self._spellslots = {'Tricks': 4,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 1}
        elif self._level == 10:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 2}
        elif self._level in [11,12]:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 2,
                                'Level6': 1}
        elif self._level in [13,14]:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 2,
                                'Level6': 1,
                                'Level7': 1}
        elif self._level in [15,16]:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 2,
                                'Level6': 1,
                                'Level7': 1,
                                'Level8': 1}
        elif self._level == 17:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 2,
                                'Level6': 1,
                                'Level7': 1,
                                'Level8': 1,
                                'Level9': 1}
        elif self._level == 18:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 3,
                                'Level6': 1,
                                'Level7': 1,
                                'Level8': 1,
                                'Level9': 1}
        elif self._level == 19:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 3,
                                'Level6': 2,
                                'Level7': 1,
                                'Level8': 1,
                                'Level9': 1}
        elif self._level == 20:
            self._spellslots = {'Tricks': 5,
                                'Level1': 4,
                                'Level2': 3,
                                'Level3': 3,
                                'Level4': 3,
                                'Level5': 3,
                                'Level6': 2,
                                'Level7': 2,
                                'Level8': 1,
                                'Level9': 1}
            
    def showInfo(self):
        super().showInfo()
        print(f'Spell Slots: {self._spellslots}')
