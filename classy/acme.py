import random
import unittest


class Product:
    def __init__(self, name= "A Cool Toy"):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(999999, 9999999)

    def stealability(self):
        steal_ratio = self.price / self.weight
        if steal_ratio < .05:
          return print("Not so stealable..")
        if steal_ratio >= .05 and steal_ratio < 1.0:
          return print('Kinda stealable...')
        else:
           print('very stealable')

    def explode(self):
        hot_ratio = self.weight * self.flammability
        if hot_ratio < 10:
            return print("...fizzle")
        if hot_ratio >= 10 and hot_ratio < 50:
            return print('...boom!')
        else:
            print("... BABOOM!!")

class BoxingGlove(Product):
    def __init__(self, weight=10):
      super().__init__(weight)

    def explode(self):
        hot_ratio =  self.weight * self.flammability
        if hot_ratio >= 0:
            return print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            return print("That tickles.")
        if self.weight >= 5 and self.weight <= 15:
            return print( "Hey that hurt!")
        else:
            print("OUCH!")
