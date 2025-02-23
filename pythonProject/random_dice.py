#Class called Dice containing function called roll(). Everytime we call this function we get a tuple.
import random
class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        # c = f"({a}, {b})"
        # print(c)
        return a, b


rolled_dice = Dice()
print(rolled_dice.roll())
