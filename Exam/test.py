from Person import Person
import random
a = 0
human1 = Person(name= 'Vasya_Joker', money = 100, mood = 50, hp= 100)
human2 = Person(name= 'Petya', money = 1000, mood = 70, hp= 90)
human3 = Person(name= 'Ivan', money = 2, mood = 100, hp= 150)
while True:
    if random.randint(1, 2) == 1:
        human1.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            hp=random.randint(-10, -5)
        )
        human2.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            hp =random.randint(-10, -5)
        )
        human3.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            hp=random.randint(-10, -5)
        )
        print(human1)
        print(human2)
        print(human3)
    else:
        human1.change_state(
            money=random.randint(-20, -10),
            mood=random.randint(50, 70),
            hp=random.randint(5, 10)
        )
        human2.change_state(
            money=random.randint(-20, -10),
            mood=random.randint(50, 70),
            hp=random.randint(5, 10)
        )
        human3.change_state(
            money=random.randint(-20, -10),
            mood=random.randint(50, 70),
            hp=random.randint(5, 10)
        )
        print(human1)
        print(human2)
        print(human3)
