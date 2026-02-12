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
        
        