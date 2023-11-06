print("Task X:\n")

"""
Polimorfism - означає можливість об'єктів різних типів вести себе однаково в специфічних контекстах.
"""

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bird(Animal):
    def make_sound(self):
        print("Tweet")

def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

dog, cat, bird = Dog(), Cat(), Bird()

animals = [dog, cat, bird]

animal_sounds(animals)
