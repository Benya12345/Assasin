from item import item
class Weapon(item):
    def __init__(self, name, stats=None,
                 durability=1, unbreakable=False, damage = 0):
        self.name = name
        self.stats = stats
        self.durability = durability
        self.unbreakable = unbreakable
        self.damage = damage
    def kdsj(self, damage):
        self.damage = self.stats / 100