
class Character:
    list_statut = []


class Player(Character):
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"[{self.name}] Position actuelle : (x={self.x}, y={self.y})")