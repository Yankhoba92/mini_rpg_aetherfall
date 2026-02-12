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
    def __init__(self, player, direction):
        self._player = player
        self._direction = direction

    def execute(self):
        next_zone = self._player.current_zone.connected_zones.get(self._direction)
        
        if next_zone:
            if next_zone.can_acces(self._player):
                self._player.current_zone = next_zone
                print(f"\n--- Vous entrez dans : {next_zone.get_name()} ---")
                print(next_zone.description)
                next_zone.random_event(self._player)
            else:
                print("L'accès à cette zone est verrouillé.")
        else:
            print("Il n'y a rien dans cette direction.")