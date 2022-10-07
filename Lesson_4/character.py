from Lesson_1.Character import Character
from item import  item


class CharacterWithItems(Character):
    def __init__(self, name, hp, damage, defence):
        Character.__init__(self, name, hp, damage, defence)
        self.weapon = None
        self.armor = None

    def set_weapon(self, item: item = None):
        self.weapon = item

    def set_armor(self, item: item = None):
        self.armor = item

    def attack(self, target):
        try:
            additional_damage = self.weapon.use()['damage']
        except Exception as error:
            additional_damage = 0
        target.take_damage(self.damage + additional_damage)
    def take_damage(self, damage):
        if self.defence > 0:
            self.hp -= abs(damage - self.defence)
        else:
            self.hp -= abs(damage)