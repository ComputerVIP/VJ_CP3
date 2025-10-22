from abc import ABC, abstractmethod
'''
Why can't you create an object from an abstract class?
    Too abstract.
How do abstract classes and abstract methods work together?
    Info stuff.
What does abc stand for?
    Abstract Base Class
What are decorators? 
    Functions that modify other functions.
What is an abstract method?
    A method that is declared, but contains no implementation.
What is a concrete method?
    A method that is fully implemented.
What is an abstract class?
    A class that contains one or more abstract methods.
How do you make an abstract method?
    Use the @abstractmethod decorator.
How can you create a class that inherits from multiple parent classes?
    List the parent classes in the class definition.
Why does the inheritance order matter?
    It determines the method resolution order (MRO).
What does the mro() method do when you call it on a class?
    It returns the method resolution order of the class.
What is Method resolution order?
    The order in which base classes are searched when executing a method.
'''

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Porpoise(Animal):
    def __init__(self, name, porpoise_status):
        super().__init__(name)
        self.porpoise_status = porpoise_status

    def make_sound(self):
        return (f"{self.name} is a porpoise and goes, 'Click, click'" if self.porpoise_status else f"{self.name} is not a porpoise")

class Jonas(Porpoise):
    def __init__(self, name, porpoise_status, age):
        super().__init__(name, porpoise_status)
        self.age = age
    
    def make_sound(self):
        return f"{self.name} is {self.age} years old and goes, 'Click, click'"

animal = Porpoise("Dolly", True)
print(animal.name)

print(animal.make_sound())

cecily = Porpoise("Cecily", False)
print(cecily.name) 

print(cecily.make_sound())

jonas = Jonas("Jonas", True, 5)
print(jonas.name)

print(jonas.make_sound())

larose = Jonas("LaRose", False, 3)
print(larose.name)