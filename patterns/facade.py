 

from models.character import Player
from patterns.command import Deplacer, Invoker


class FacadeInterface:
    def __init__(self):
        self.player = Player("Hero")
        self.invoker = Invoker()

    def move_player(self, dx, dy):
        command = Deplacer(self.player, dx, dy)
        self.invoker.setCommand(command)
        self.invoker.execute()

    def run(self):
        print("Commandes : 1: Avancer, 2: Reculer, 3: Gauche, 4: Droite, 0: Quitter")
        while True:
            choix = input("\nVotre choix : ")

            if choix == "1":
                self.move_player(0, 1)
            elif choix == "2":
                self.move_player(0, -1)
            elif choix == "3":
                self.move_player(-1, 0)
            elif choix == "4":
                self.move_player(1, 0)
            elif choix == "0":
                print("Fin de la partie.")
                break
            else:
                print("Choix invalide, réessayez.")
