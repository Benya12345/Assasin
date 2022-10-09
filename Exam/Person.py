class NegativeMoney(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class NegativeHp(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class NegativeMood(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Person:
    def __init__(self, name, hp, mood, money):
        self.name = name
        self.hp = hp
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' money:{self.money},' \
               f' mood: {self.mood})'

    def change_state(self, hp, mood, money):
        self.hp +=(hp)
        self.mood +=(mood)
        self.money +=(money)
        if self.money < 0:
            raise NegativeMoney('Вы банкрот!')
        if self.mood < 0:
            raise NegativeMood('Вы в дипресии!')
        if self.hp < 0:
            raise NegativeHp('Вы умерли! XD')

