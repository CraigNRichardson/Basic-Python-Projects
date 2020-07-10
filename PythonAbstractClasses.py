from abc import ABC, abstractmethod

class Life(ABC):
    def era(self, birth, death):
        print("Person object created...")

    @abstractmethod
    def years(self, birth, death):
        pass

class Person(Life):
    def years(self, birth, death):
        print("George Washington was born in {} and died in {} ".format(birth, death))

if __name__ == "__main__":
    person = Person()
    person.era("1732","1799")
    person.years("1732","1799")
        
