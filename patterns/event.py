from enum import Enum
from abc import ABC, abstractmethod
import random

from models.items import ItemFactory
from patterns.enemy import EnemyFactory

class EventType(Enum):
    COMBAT = "combat"
    COFFRE = "coffre"
    MARCHAND = "marchand"
    DIALOGUE = "dialogue"
    

class Event(ABC):
    def __init__(self, event_type: EventType, description: str):
        self.event_type = event_type
        self.description = description
    
    @abstractmethod
    def trigger(self):
        print(f"Événement déclenché: {self.description}")

    def get_description(self):
        return self.description

class CombatEvent(Event):
    def __init__(self, enemy_type):
        super().__init__(
            event_type = EventType.COMBAT,
            description = f"Un {enemy_type.name} vous attaque!")
        self.enemy_type = enemy_type

        
    def trigger(self, player):
        print(f"Le joueur {player.name} apparait")
        while self.enemy_type.is_alive() and player.pv > 0: 

            self.enemy_type.attack(player)
            print("1. Attaquer")
            print("2. Compétences")
            print("3. Objet")
            print("4. Défendre")

            choix = input("Choisissez une action: ")
            if choix == "1":
                damage = player.force
                print(f"{player.name} attaque {self.enemy_type.name} pour {damage} dégâts!")
                self.enemy_type.take_damage(damage)
                if not self.enemy_type.is_alive():
                    player.argent += self.enemy_type.argent
                    print(f"{player.name} gagne {self.enemy_type.argent} pièces d'or! (Or total: {player.argent})")
                    print(f"{self.enemy_type.name} est vaincu!")
                    break

            elif choix == "2":
                print("lmao")
            elif choix == "3":
                print("lmao")
            elif choix == "4":
                print(f"{player.name} se prépare à défendre.")
        
        return self.enemy_type

class CoffreEvent(Event):
    def __init__(self, recompense: None):
        super().__init__(
            event_type = EventType.COFFRE,
            description = "Vous trouvez un coffre!"
        )
        self.recompense = recompense or self.recompense_random()
        self.opened = False
    
    def trigger(self, player):
        if self.opened:
            self.opened = True
            print(f"Le coffre a été ouvert par {player.name}!")
            return self.recompense
        else:
            print("Le coffre est fermé.")
            choix = input("Voulez-vous l'ouvrir? (oui/non) ").lower()
            if choix == "oui":
                self.opened = True
                print(f"{player.name} a ouvert le coffre et trouve : {self.recompense}!")
                
                item = ItemFactory.createItem(self.recompense, consommable=True)
                
                player.takeItem(item)
                return self.recompense
            else:
                print("Vous décidez de ne pas ouvrir le coffre.")
                return None
            

    
    def recompense_random(self):
        items = ["Potion de soin", "Épée en fer", "Armure légère", "Anneau de force"]
        return random.choice(items, random.randint(1, 3))

class MarchandEvent(Event):
    def __init__(self):
        super().__init__(
            event_type = EventType.MARCHAND,
            description = "Vous rencontrez un marchand ambulant."
        )
        self.inventory={
            "Potion de soin": 10,
            "Épée en fer": 50,
            "Armure légère": 40,
            "Anneau de force": 30
        }
    
    def trigger(self, player):
        print(f"Le marchand propose ses marchandises à {player.name}.")
        for item, price in self.inventory.items():
            print(f"{item}: {price} pièces d'or")
        return self.inventory
    
    def buyItem(self, player, item_name):
        if item_name in self.inventory:
            price = self.inventory[item_name]
            if player.gold >= price:
                player.gold -= price
                print(f"{player.name} a acheté {item_name} pour {price} pièces d'or.")
                return item_name
            else:
                print("Vous n'avez pas assez d'or.")
                return None
        else:
            print("L'article n'est pas disponible.")
            return None

class DialogueEvent(Event):
    def __init__(self, npc_name, dialogue):
        super().__init__(
            event_type = EventType.DIALOGUE,
            description = f"Vous rencontrez {npc_name}."
        )
        self.npc_name = npc_name
        self.dialogue = dialogue
    
    def trigger(self, player):
        print(f"{self.npc_name}: {self.dialogue}'")
        return self.dialogue
    
class EventFactory:

    def create_event(self, event_type: EventType, **kwargs):
        if event_type == EventType.COMBAT:
            return CombatEvent(kwargs.get('enemy_type'), kwargs.get('description', "Un ennemi vous attaque!"))
        elif event_type == EventType.COFFRE:
            return CoffreEvent(kwargs.get('recompense'))
        elif event_type == EventType.MARCHAND:
            return MarchandEvent()
        elif event_type == EventType.DIALOGUE:
            return DialogueEvent(kwargs.get('npc_name'), kwargs.get('dialogue'))
        else:
            raise ValueError("Invalid event type")