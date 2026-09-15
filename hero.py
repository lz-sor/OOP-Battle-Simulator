import random
from goblin import Goblin
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__ (self, name):
        self.name = name
        self.health = 125
        self.attack_power = 20

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        if self.health == 0:
            return False
        else:
            return True
    def counterStrike(self, enemy):
        print("Your hero lands a counter strike!")
        enemy.take_damage(self.attack())

    def defend(self, enemy: Goblin):
        conditional = random.randint(1,10)
        if conditional > 1:
            newAttack = enemy.attack() - 10
            if newAttack < 0:
                newAttack = 0
            print(f"{enemy.name} attacks!")
            self.take_damage(newAttack)
        elif conditional == 1:
            print("Hero defense failed!")
            self.take_damage(enemy.attack())
        if random.randint(1,10) < 3:
            print("")
            self.counterStrike(enemy)
