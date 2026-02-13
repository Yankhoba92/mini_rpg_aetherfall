from enum import Enum
from abc import ABC, abstractmethod
import random
from enemy import EnemyFactory

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
    def __init__(self, enemy_type, description):
        super().__init__(
            event_type = EventType.COMBAT,
            description = f"Un {enemy_type.value} vous attaque!")
        
    def trigger(self, player):
        print(f"Le joueur {player.name} apparait")
        factory = EnemyFactory()
        enemy = factory.create_enemy(self.enemy_type)
        return enemy

class CoffreEvent(Event):
    def __init__(self, recompense: None):
        super().__init__(
            event_type = EventType.COFFRE,
            description = "Vous trouvez un coffre!"
        )
        self.recompense = recompense or self.recompense_random()
        self.opened = False
    
    def trigger(self, player):
        if not self.opened:
            self.opened = True
            print(f"Le coffre a été ouvert par {player.name}!")
            return self.recompense
        else:
            print("Le coffre est déjà ouvert.")
            return None
    
    def recompense_random(self):
        items = ["Potion de soin", "Épée en fer", "Armure légère", "Anneau de force"]
        return random.choice(items, random.randint(1, 3))
    