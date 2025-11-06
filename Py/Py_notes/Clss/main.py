'''
What is a parent/abstract class?
    A class that is inherited by other classes.
How do you create a child class?
    By passing the parent class as a parameter in the child class definition.
How does a child class inherit from the parent class?
    It inherits all attributes and methods of the parent class.
What are class diagrams?
    Visual representation of classes and their relationships.
How are class diagrams used to show a parent/child relationship?
    By using white arrows to indicate inheritance.
How do you overload operators in a class?
    By defining special methods like __add__, __sub__, etc.
What are test cases?    
    Make sure your code works as expected.
Why do we use test cases?
    To test if classes ain't broke.
How do we create test cases?
    By using a testing framework like unittest or pytest.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."
    
# Example usage
person = Person("Alice", 30)
print(person.greet())
student = Student("Bob", 20, "S12345")
print(student.greet())
print(student.study())