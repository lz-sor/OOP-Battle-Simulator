from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Void"
hero = Hero("Loki-(L1130)")
hero2 = Hero("spare")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Variant")
    goblin2 = Goblin("Variant 2")
    
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    print("")

    goblin.take_damage(hero.attack())

    print("")

    if goblin.is_alive:
        hero.take_damage(goblin.attack())
 # type: ignore


if __name__ == "__main__":
    main()