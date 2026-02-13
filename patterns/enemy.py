from __future__ import annotations

from enum import Enum
from abc import ABC, abstractmethod
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.character import Player
class EnemyType(Enum):
    Loup_sauvage = "loup_sauvage"
    Bandit = "bandit"
    Squelette = "squelette"
    Champion_corrompu = "champion_corrompu"
    Gardien_donjon = "gardien_donjon"

#  INTERFACE IENEMY 
class IEnemy(ABC):    
    def __init__(self, name: str, pv: int, enemy_type: EnemyType, description: str, argent: int = 10):
        self.name = name
        self.pv = pv
        self.type = enemy_type
        self.description = description
        self.current_hp = pv
        self.argent = argent
    
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
    

    
class LoupSauvage(IEnemy):    
    def __init__(self):
        super().__init__(
            name="Loup sauvage",
            pv=50,
            enemy_type=EnemyType.Loup_sauvage,
            description="Un loup féroce aux yeux rouges."
        )
        self.attack_power = 15
    
    def spawn(self, zone):
        super().spawn(zone)
    
    def attack(self, target: Player):
        damage = self.attack_power
        print(f"{self.name} mord {target.name} pour {damage} dégâts!")
        target.take_damage(damage)
        return damage


class Bandit(IEnemy):    
    def __init__(self):
        super().__init__(
            name="Bandit",
            pv=60,
            enemy_type=EnemyType.Bandit,
            description="Un voleur sans scrupules.",
            argent=15
        )
        self.attack_power = 18
    
    def spawn(self, zone):
        super().spawn(zone)
    
    def attack(self, target: Player):
        damage = self.attack_power
        print(f"{self.name} attaque {target.name} avec sa dague pour {damage} dégâts!")
        target.take_damage(damage)
        return damage


class Squelette(IEnemy):    
    def __init__(self):
        super().__init__(
            name="Squelette",
            pv=70,
            enemy_type=EnemyType.Squelette,
            description="Ossements animés par magie noire.",
            argent=20
        )
        self.attack_power = 12
    
    def spawn(self, zone):
        super().spawn(zone)
    
    def attack(self, target: Player):
        damage = self.attack_power
        print(f"{self.name} frappe {target.name} pour {damage} dégâts!")
        target.take_damage(damage)
        return damage


class ChampionCorrompu(IEnemy):    
    def __init__(self):
        super().__init__(
            name="Champion corrompu",
            pv=150,
            enemy_type=EnemyType.Champion_corrompu,
            description="Guerrier d'élite corrompu par les ténèbres.",
            argent=50
        )
        self.attack_power = 30
    
    def spawn(self, zone):
        super().spawn(zone)
    
    def attack(self, target: Player):
        damage = self.attack_power
        print(f"{self.name} frappe puissamment {target.name} pour {damage} dégâts!")
        target.take_damage(damage)
        return damage


class GardienDonjon(IEnemy):    
    def __init__(self):
        super().__init__(
            name="Gardien du donjon",
            pv=300,
            enemy_type=EnemyType.Gardien_donjon,
            description="Gardien ancestral du donjon. Devient furieux à mi-combat.",
            argent=75
        )
        self.attack_power = 40
        self.phase = 1
    
    def spawn(self, zone):
        super().spawn(zone)
    
    def attack(self, target: Player):
        # Phase 2 si moins de 50% HP
        if self.current_hp < self.pv / 2 and self.phase == 1:
            self.phase = 2
            print(f"\n⚡ {self.name} entre en PHASE 2!")
            self.attack_power = 55
        
        damage = self.attack_power
        phase_text = " avec FUREUR" if self.phase == 2 else ""
        print(f"{self.name} attaque{phase_text} {target.name} pour {damage} dégâts!")
        target.take_damage(damage)
        return damage


class EnemyFactory:
    def __init__(self):
        self.enemy_types = {
            EnemyType.Loup_sauvage: LoupSauvage,
            EnemyType.Bandit: Bandit,
            EnemyType.Squelette: Squelette,
            EnemyType.Champion_corrompu: ChampionCorrompu,
            EnemyType.Gardien_donjon: GardienDonjon
        }
    

    def create_enemy(self, enemy_type):
        enemy_class = self.enemy_types.get(enemy_type)
        if enemy_class:
            return enemy_class()
        else:
            raise ValueError(f"Type d'ennemi inconnu: {enemy_type}")
        
    def create_random_enemy(self):
        
        enemy_type = random.choice(list(self.enemy_types.keys()))
        return self.create_enemy(enemy_type)
        
    def register_enemy(self, enemy_type, enemy_class):
        self.enemy_types[enemy_type] = enemy_class