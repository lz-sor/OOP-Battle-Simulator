from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Void"
hero = Hero("Loki-(L1130)")

goblin = Goblin("Variant")
goblin2 = Goblin("Variant 2")

def battleDecision(enemy: Goblin):
    decision = input("But the battle isn't over yet! Do you, 'hero', choose to defend or attack? ")
    if decision[:6].lower() == "attack":
        print("")
        print(f"You choose to attack the {enemy.name}!")
        enemy.take_damage(hero.attack())
    else:
        print("")
        print("You choose to defend!")
        hero.defend(enemy)
    return decision[:6].lower()

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        decision2 = battleDecision(enemy)
        if enemy.is_alive() and decision2 == "attack":
            print(f"{enemy.name} fires back!")
            hero.take_damage(enemy.attack())
    if hero.is_alive():
        print(f"{hero.name} wins the battle!")
    else:
        print(f"Your hero is a loser, they lost to {enemy.name}")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Well done, you're another loser that's been pruned, so welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("You've been wandering for hours when you hear footsteps approaching...")
    
    print(f"{goblin.name} comes into view, with {goblin.health} health.")
    print(f"{goblin2.name} (because what else are you supposed to call him? Loki? That's weird) follows with {goblin2.health} health.")
    print(f"{hero.name} steps into view (like an idiot) with {hero.health} health.")

    print("")

    print(f"{hero.name} ATTACKS the {goblin.name}! What a TREMENDOUS idea.")
    goblin.take_damage(hero.attack())

    print("")

    if goblin.is_alive:
        print(f"{goblin.name} (in self defense, mind you) attacks {hero.name}!")
        hero.take_damage(goblin.attack())
        print("")

    battle(hero, goblin)

    print("Hope you're happy with yourself, 'hero'.")
    print("")
    print("Tutorial Over.")

 # type: ignore


if __name__ == "__main__":
    main()