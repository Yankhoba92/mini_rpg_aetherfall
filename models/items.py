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
    def __init__(self, name: str, consommable: bool = False, atk: int = 0, magic: int = 0):
        super().__init__(name, consommable)
        self.attack = atk
        self.magic_attack = magic
    
class Armure(Item):
    def __init__(self, name: str, consommable: bool = False, defense: int = 0, magic_defense: int = 0):
        super().__init__(name, consommable)
        self.defense = defense
        self.magic_defense = magic_defense



class Bombe(Item):
    def __init__(self, name: str = "bombe", consommable: bool = True):
        super().__init__(name, consommable)
    
    def explode(self, player, target):
        print(f"Hero a utilisé une {self.name} et a causé une explosion sur {target.name}!")

    
class ItemFactory(Item):
    
    @staticmethod
    def createItem(name: str, consommable: bool, atk: int = 0, magic: int = 0, defense: int = 0, magic_defense: int = 0):
        if name == "potion":
            return Potion(name, consommable)
        elif name == "antidote":
            return Antidote(name, consommable)
        elif name == "bombe":
            return Bombe(name, consommable)
        elif name == "arme":
            return Arme(name, consommable, atk, magic)
        elif name == "armure":
            return Armure(name, consommable, defense, magic_defense)
        elif name == "item":
            return Item(name, consommable)
        else: 
            raise ValueError("Invalid item name")
    


if __name__ == "__main__":
    potion = ItemFactory.createItem("arme", False, atk=10, magic=5)
    print(f"Crée l'item: {potion.name}, Attack: {potion.attack}, Magic: {potion.magic_attack}")





