from abc import ABC


class Item(ABC):
    def __init__(self, name: str, consommable: bool):
        self.name = name
        self.consommable = consommable

class Potion(Item):
    def __init__(self, name: str = "potion", consommable: bool = True):
        super().__init__(name, consommable)
    
    def heal(self, player):
        print(f"Hero a utilisé une {self.name} et a récupéré de la santé!")

class Antidote(Item):
    def __init__(self, name: str = "antidote", consommable: bool = True):
        super().__init__(name, consommable)
    
    def cure(self, player):
        print(f"Hero a utilisé une {self.name} et a été guéri de l'empoisonnement!")

class Arme(Item):
    def __init__(self, name: str = "arme", consommable: bool = False):
        super().__init__(name, consommable)
    
    def attack(self, player, target):
        print(f"Hero a utilisé une {self.name} pour attaquer {target.name}!")

class Bombe(Item):
    def __init__(self, name: str = "bombe", consommable: bool = True):
        super().__init__(name, consommable)
    
    def explode(self, player, target):
        print(f"Hero a utilisé une {self.name} et a causé une explosion sur {target.name}!")

    
class ItemFactory(Item):
    
    @staticmethod
    def createItem(name: str, consommable: bool):
        if name == "potion":
            return Potion(name, consommable)
        elif name == "antidote":
            return Antidote(name, consommable)
        elif name == "bombe":
            return Bombe(name, consommable)
        else: 
            raise ValueError("Invalid item name")
    


if __name__ == "__main__":
    potion = ItemFactory.createItem("potion", True)
    potion.heal("Hero")





