#MAIN CLASS         -> DEFINES A CHARACTER, IT'S ATTRIBUTES E ACTIONS
#CLASSE PRINCIPAL   -> DEFINE UM PERSONAGEM, SEUS ATRIBUTOS E AÇÕES

from random import randint

class Character():
    def __init__(self, name, genre, age):   #CHARACTER'S STATUS
        self._level          = 1                                                                           #STATUS DO PERSONAGEM
        self.name            = name                                                                              
        self.genre           = genre
        self.age             = age
        self._strength       = self.setStatus()
        self._dexterity      = self.setStatus()
        self._charism        = self.setStatus()
        self._wisdom         = self.setStatus()
        self._intelligence   = self.setStatus()
        self._constitution   = self.setStatus()
        self._hp             = 0
        self._proficiency    = 2
        
    def setStatus(self):
        statusPoints = []
        for i in range(4):
            rollDice = randint(1,6)
            statusPoints.append(rollDice)
        statusPoints.remove(min(statusPoints))
        statusResult = sum(statusPoints)
        return statusResult

    def showInfo(self):
        print(f'Name: {self.name.ljust(20)} | Level: {str(self._level).ljust(20)} | Genre: {self.genre.ljust(20)} | Age: {str(self.age).ljust(20)} | HP: {str(self._hp).ljust(10)} | Proficiency Bonus: +{self._proficiency}')
        print(f'STR: {str(self._strength).ljust(5)} | DEX: {str(self._dexterity).ljust(5)} | CHA: {str(self._charism).ljust(5)} | WIS: {str(self._wisdom).ljust(5)} | INT: {str(self._intelligence).ljust(5)} | CON: {str(self._constitution).ljust(5)}')
        
    def levelUp(self):
        self._level += 1
        if self._level in [1,2,3,4]:
            self._proficiency = 2
        elif self._level in [5,6,7,8]:
            self._proficiency = 3
        elif self._level in [9,10,11,12]:
            self._proficiency = 4
        elif self._level in [13,14,15,16]:
            self._proficiency = 5
        else:
            self._proficiency = 6