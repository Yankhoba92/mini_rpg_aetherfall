 

from models.character import Guerrier, Mage, Player
from models.zone import Donjon, Foret, Village, Zone
from patterns.command import Deplacer, Invoker


class FacadeInterface:
    def __init__(self):
        self.village = Village("Village d'Aether", "Un lieu sûr.", has_merchant=True)
        self.foret = Foret("Forêt Sombre", "Peuplée de créatures sauvages.", danger_level=2)
        self.donjon = Donjon("Donjon d'Émeraude", "Le repaire du Gardien.", total_room=3)

        self.village.add_connection("nord", self.foret)
        self.foret.add_connection("sud", self.village)
        self.foret.add_connection("nord", self.donjon)
        
        name_perso = input("Entrez votre nom de personnage : ")
        self.player = Player(name_perso)
        print("Choisissez votre classe :")
        print("1. Guerrier")
        print("2. Mage")
        print("3. Voleur")
        classe_choix = input("Entrez le numéro de votre classe : ")
        self.player = self.player.chooseClass(classe_choix)
        
        self.player.current_zone = self.village
        self.invoker = Invoker()
        
    
   
    def run(self):
        print(f"Bienvenue dans Aetherfall, {self.player.name}.")
        print(f"Vous allez commencer votre aventure en tant que {self.player.classe}.\n")
        print("PV:", self.player.pv)
        print("Force:", self.player.force)
        while True:
            current = self.player.current_zone
            print(f"Position actuelle : {current.get_name()} \n")
            print(current.description)
            
            current.random_event(self.player)

            sorties = ", ".join(current.connected_zones.keys())
            print(f"Sorties : {sorties}")
            choix = input("Action (direction ou 'quitter') : ").lower()

            if choix == "quitter":
                break
            elif choix in current.connected_zones:
                cmd = Deplacer(self.player, choix)
                self.invoker.setCommand(cmd)
                self.invoker.execute()
            else:
                print("Action impossible.")