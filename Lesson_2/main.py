from Lesson_1.Character import Character
from berserk import Berserk
from Assasin import Assasin

p1 = Berserk(name='Berserk', hp=100, damage=8, armor=0)
p2 = Assasin(name='Assasin', hp=100, damage=10, armor=0)

while p1.hp > 0 and p2.hp > 0:
    print(p1)
    print(p2)
    p1.attack(p2)
    p2.attack(p1)
    print()