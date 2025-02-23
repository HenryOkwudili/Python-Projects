# Make a class Dice containing a function roll to roll two dices randomly


import random
class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        return a, b

rolled_dice = Dice()
print(rolled_dice.roll())