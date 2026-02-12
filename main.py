class Invoker:
    def __init__(self):
        self._command = None
    
    def setCommand(self, command):
        self._command = command
    
    def execute(self):
        if self._command:
            self._command.execute()

class Command:
    def execute(self):
        pass

class Deplacer(Command):
    def __init__(self, player, x, y):
        self._player = player
        self._x = x
        self._y = y

    def execute(self):
        self._player.move(self._x, self._y)

class Player:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"[{self.name}] Position actuelle : (x={self.x}, y={self.y})")

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

if __name__ == "__main__":
    game = FacadeInterface()
    game.run()