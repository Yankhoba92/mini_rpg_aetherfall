
from typing import List

from models.items import Item


class Character:
    list_statut = []


class Player(Character):

    def __init__(self, name):
            self.name = name
            self.current_zone = None


    
    def useItem(self, item: Item):
        if item in self.inventory:
            if isinstance(item, Item):
                if item.consommable:
                    self.inventory.remove(item)
                print(f"{self.name} a utilisé {item.name}!")
            else:
                print(f"{item.name} n'est pas un objet utilisable.")
        else:
            print(f"{item.name} n'est pas dans l'inventaire de {self.name}.")

    def takeItem(self, item: Item):
        self.inventory.append(item)
        print(f"{self.name} a pris {item.name}!")

if __name__ == "__main__":
    player = Player("Hero")
    potion = Item("potion", True)
    player.takeItem(potion)
    print(f"Inventaire de {player.name} : {[item.name for item in player.inventory]}")
    player.useItem(potion)

    print(f"Inventaire de {player.name} : {[item.name for item in player.inventory]}")