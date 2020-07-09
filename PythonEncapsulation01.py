
class Human:
    def __init__(self):
        self._currentAge = 0

    def __init__(self):
        self.__maxAge = 36

    def getMaxAge(self):
        print("Max Age:",self.__maxAge)

    def setMaxAge(self, maxAge):
        self.__maxAge = maxAge
    

if __name__ == "__main__":

    john = Human()
    john._currentAge = 34
    print("Current Age:",john._currentAge)

    john.getMaxAge()
    john.setMaxAge(120)
    john.getMaxAge()
