
from __future__ import annotations

from abc import ABC
from typing import List, TYPE_CHECKING

from models.items import Item

if TYPE_CHECKING:
    from patterns.enemy import IEnemy


class Character:
    list_statut = []


class Player(Character):

    def __init__(self, name, classe=None):
            self.name = name
            self.classe = classe
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

    def useSkill(self, skill, cible: IEnemy):
        print(f"{self.name} a utilisé la compétence {skill.name} sur {cible.name}!")
    
    def useSkill2(self, skill, cible: IEnemy):
        print(f"{self.name} a utilisé la compétence {skill.name} sur {cible.name}!")

    def getClasse(self):
        return self.classe

    def chooseClass(self, class_choix):
        if class_choix == "1":
            return Guerrier(self.name)
        elif class_choix == "2":
            return Mage(self.name)
        elif class_choix == "3":
            return Voleur(self.name)
        else:
            print("Choix invalide, classe par défaut : Guerrier.")
            return Guerrier(self.name)
        
        
    def get_stats(self):
        return {
            "PV": self.pv,
            "Force": self.force,
            "Magie": self.magie,
            "Défense": self.defense,
            "Taux de critique": self.taux_critique
        } 
        

    def take_damage(self, amount: int):
        self.pv -= amount
        if self.pv < 0:
            self.pv = 0
        print(f"{self.name} subit {amount} dégâts! (PV: {self.pv}/{self.max_pv})")
        if self.pv <= 0:
            print(f"{self.name} est mort!")
            exit()
        

class Guerrier(Player):    
    def __init__(self, name):
        super().__init__(name, "Guerrier")
        self.max_pv = 150
        self.pv = self.max_pv
        self.force = 20
        self.magie = 0
        self.taux_critique = 1

        self.defense = 15
        self.inventory = []

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage")
        self.max_pv = 80
        self.pv = self.max_pv
        self.force = 5
        self.magie = 40
        self.defense = 0
        self.magic_force = 30
        self.taux_critique = 1
        self.inventory = []

class Voleur(Player):
    def __init__(self, name):
        super().__init__(name, "Voleur")
        self.max_pv = 100
        self.pv = self.max_pv
        self.force = 15
        self.magie = 0
        self.defense = 10
        self.taux_critique = 1.25
        self.inventory = []
        
        



if __name__ == "__main__":
    player = Player("Hero", "Guerrier")
    potion = Item("potion", True)
    player.takeItem(potion)
    print(f"Inventaire de {player.name} : {[item.name for item in player.inventory]}")
    player.useItem(potion)

    print(f"Inventaire de {player.name} : {[item.name for item in player.inventory]}")