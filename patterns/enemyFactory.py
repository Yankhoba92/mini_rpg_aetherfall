from enum import Enum
from abc import ABC, abstractmethod
class EnemyType(Enum):
    Loup_sauvage = "loup_sauvage"
    Bandit = "bandit"
    Squelette = "squelette"
    Champion_corrompu = "champion_corrompu"
    Gardien_donjon = "gardien_donjon"

#  INTERFACE IENEMY 
class IEnemy(ABC):    
    def __init__(self, name: str, pv: int, enemy_type: EnemyType, description: str):
        self.name = name
        self.pv = pv
        self.type = enemy_type
        self.description = description
        self.current_hp = pv
    
    @abstractmethod
    def spawn(self, zone):
        print(f"\n{self.name} apparaît dans {zone}!")
        print(f"{self.description}")
    
    @abstractmethod
    def attack(self, target):
        pass
    
    def take_damage(self, amount: int):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.name} subit {amount} dégâts! (PV: {self.current_hp}/{self.pv})")
    
    def get_comportement(self):
        return "attaque"  # Comportement par défaut
    
    def is_alive(self) -> bool:
        return self.current_hp > 0 # Verifie si l'ennemi est encore en vie
