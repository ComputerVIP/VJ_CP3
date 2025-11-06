from main import *

def test_Person():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30
    assert p.greet() == "Hello, my name is Alice and I am 30 years old."