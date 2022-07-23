"""
----
SETS
----
"""

import sys
import os

#  Set is a collection data type which is unordered and mutable,
#  no duplicate elements

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set, "\n")  # To show that sets don't have duplicates

myset = set([1, 2, 4])  # Iterable?
print(myset, "?\n")

myset2 = set("Hello")  # Interesting.
print(myset2, "\n")  # Helps us to see the unique characters
# present in a string


myset3 = {}
print(type(myset3), "\n")  # Returns dict so be careful

myset4 = set()
print(type(myset4), "\n")  # Returns Empty set

myset4.add(1)
myset4.add(2)
myset4.add(3)
myset4.add(4)
myset4.add(5)
print(myset4, ".add(numbers)\n")

myset4.remove(3)
print(myset4, ".remove(3)\n")

"""
myset4.remove(69)
print(myset4)  # Returns key error because token doesn't
# exist in the set
"""

myset4.discard(69)
print(myset4, ".discard()\n")  # Doesn't return error because discard is cool

"""
myset4.clear()
print(myset4)  # Clears the set of its elements
"""

print(myset4.pop(), "\n")  # Removes an item and removes it
print(myset4, ".pop()\n")

for x in myset4:
    print(x, "printing all items in the set\n")  # Duh

for x in range(1, 70):
    if x in myset4:
        print(x, "= YEET + exists + range of 69 is very funny\n")

what = input("Would u like to clear the console(y/n): ")
if what == "y":
    os.system('clear')
elif what == "n":
    print("k")
else:
    print("I am blue da ba dee da ba diee da ba dee da ba DIEE!")
    sys.exit(1)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

print("\n")

print(odds, "Set of odds\n")
print(evens, "Set of evens\n")
print(primes, "Set of primes\n")

u = odds.union(evens)
print(u, "Union of odds and evens sets\n")

I_o_e = odds.intersection(evens)
print(I_o_e, "Intersection of odds and evens (doesn't happen)\n")

I_o_p = odds.intersection(primes)
print(I_o_p, "Intersection of odds and primes\n")

I_o_e = evens.intersection(primes)
print(I_o_p, "Intersection of evens and primes\n")
