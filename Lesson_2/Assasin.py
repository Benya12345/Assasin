from Lesson_1.Character import Character
import random
class Assasin(Character):
    def __init__(self, name, hp, damage, armor):
        Character.__init__(self, name, hp, damage, armor)

    def xp(self):
        return(self.max_hp - self.hp) * 0.1
    def attack(self, target):
        target.take_damage(self.damage - self.xp())
