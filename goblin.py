import random
from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 100, 7)
        self.gold = 0

    def stealGold(self, hero):
        """STEAL'N GOOD PEOPLE's DOUGH"""
        print("Gimme the bread")
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("GIT REkT NOOB")