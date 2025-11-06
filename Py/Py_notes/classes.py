#Vincent J
'''
What is a class?
    A blueprint for creating objects. A class encapsulates data for the object.
What is an object?
    Instance of a class.
How is a class a form of encapsulation? 
    Bundling data and methods that operate on that data within one unit.
How is a class an abstraction of an object?
    Hides complex implementation details and shows only the necessary parts.
How do you access information in an object?
    self.
How do you initialize a class?
    Using the __init__ method.
How do you set a default value 
    name = "John", but variables with defaults must come after non-defaults.
How do you use type hinting?
    name: str, age: int
How do you set an attribute to be private?
    Using underscores _ before the attribute name.
How do you make a class method?
    def name(self):
Why do we include docstrings/
    Best practice for documentation.
What does "self" do as a parameter for class methods?
    Tells it to use the instance of the object.
What are getter and setter methods?
    Get and set values.
What are magic methods?
    __init__, __str__, __repr__, __len__, etc.
Where are class objects saved? (heap or stack?)
    Heap
'''
class Perosn:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name} {self.last} and I am {self.age} years old.")

    def setAge(self):
        self.age +=1


p1 = Perosn("John", "Doe", 36)
cecily = Perosn("Cecily", "Strong", 30)

cecily.setAge()
print(cecily.age)