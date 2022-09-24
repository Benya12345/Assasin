from Lesson_1.Character import Character
import random
class Assasin(Character):
    def __init__(self, name, hp, damage, armor):
        Character.__init__(self, name, hp, damage, armor)

    def attack(self, target):
        target.take_damage(self.damage)
        if(random.randint(1, 3) == 3):
            target.take_damage(self.damage + 1000)




