"""
-----------------------
Testing / Learning File
-----------------------
"""

# Imports and From-Imports
import openpyxl
from pathlib import Path

# Try and Except Construct
"""
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")
"""

"""
-------
Classes
-------
"""

"""
class Point:
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
"""

# Inheritance

"""
class Mammal: # Parent Class
    def walk(self):
        print("Walk")


class Dog(Mammal): # Inherits Mammal walk method
    def bark(self): # Bark method applies only to Dog class
        print("Bark")


class Cat(Mammal): # Inherits Mammal walk method
    def meow(self): # Meow method applies only to cat class
        print("Meow")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meow()
"""

"""
path = Path()
for file in path.glob('*'):
    print(f"{file} path.glob('*')")
for file in path.glob('*.*'):
    print(f"{file} path.glob('*.*')")
"""

"""
a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]# Squares each element in the referenced list
      |       |
# expression  |
# for loop to loop through list  

print(a)
print(b)
"""




