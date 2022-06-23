"""
-----------------
Personal Solution
-----------------
"""
import random

"""
class Dice:
    def roll(self):
        rand_list = []
        for num in range(2):
            a = random.randint(1, 7)
            rand_list.append(a)
        rand_list_tuple = tuple(rand_list)
        return rand_list_tuple


while True:
    roll1 = Dice()
    print(roll1.roll())
"""

"""
---------------
Mosh's Solution
---------------
"""

"""
class Dice:
    def roll(self):
        first = random.randint(1, 7)
        second = random.randint(1, 7)
        return first, second


dice = Dice()
print(dice.roll())
"""