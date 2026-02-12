from abc import ABC, abstractmethod
from enum import Enum

class ZoneType(Enum):
    VILLAGE = "village"
    FORET = "foret"
    DONJON = "donjon"

class Zone(ABC):
    
    def __init__(self, name: str, description: str, zone_type: ZoneType):
        self.name = name
        self.description = description
        self.type = zone_type
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
    
    @abstractmethod
    def trigger_random_event(self):
        pass
    
    @abstractmethod
    def can_access(self, player) -> bool:
        pass
    
    def get_name(self) -> str:
        return self.name


class Village(Zone):    
    def __init__(self):
        super().__init__(
            name="Village",
            description="Un village paisible. Le marchand vous attend sur la place.",
            zone_type=ZoneType.VILLAGE
        )
    
    def trigger_random_event(self):
        import random
        events = ["marchand", "dialogue", "repos"]
        return random.choice(events)
    
    def can_access(self, player) -> bool:
        return True


class Foret(Zone):    
    def __init__(self):
        super().__init__(
            name="Forêt",
            description="Une forêt sombre et dangereuse.",
            zone_type=ZoneType.FORET
        )
    
    def trigger_random_event(self):
        import random
        rand = random.random()
        
        if rand < 0.6:
            return "combat"
        elif rand < 0.9:
            return "coffre"
        else:
            return "rien"
    
    def can_access(self, player) -> bool:
        """Toujours accessible"""
        return True


class Donjon(Zone):
    
    def __init__(self):
        super().__init__(
            name="Donjon",
            description="Un donjon terrifiant. Le boss vous attend.",
            zone_type=ZoneType.DONJON
        )
        self.current_room = 0
        self.total_rooms = 2
    
    def trigger_random_event(self):
        if self.current_room < self.total_rooms:
            return "combat"
        else:
            return "boss"
    
    def can_access(self, player) -> bool:
        # Vérifier si le joueur a la clé
        if hasattr(player, 'inventory'):
            for item in player.inventory:
                if item == "Clé du Donjon":
                    return True
            print("Vous avez besoin de la Clé du Donjon!")
            return False
        return False
    
    def next_room(self):
        """Passe à la salle suivante"""
        self.current_room += 1
        print(f"Vous avancez... Salle {self.current_room}/{self.total_rooms}")

