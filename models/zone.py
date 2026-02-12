import random

class Zone:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.event_list = []
        self.connected_zones = {} 

    def add_event(self, event):
        self.event_list.append(event)
        
    def add_connection(self, direction, zone):
        self.connected_zones[direction] = zone

    def get_name(self):
        return self.name

    def random_event(self, player):
        if self.event_list and random.random() < 0.4:
            event = random.choice(self.event_list)
            print(f"[Événement] {event.get_description()}  \n")
            event.declencher(player)

    def can_acces(self, player):
        return True

class Village(Zone):
    def __init__(self, name, description, has_merchant=True):
        super().__init__(name, description)
        self.has_merchant = has_merchant

class Foret(Zone):
    def __init__(self, name, description, danger_level=1):
        super().__init__(name, description)
        self.danger_level = danger_level

class Donjon(Zone):
    def __init__(self, name, description, total_room=3):
        super().__init__(name, description)
        self.total_room = total_room 
        self.current_room = 0

    def next_room(self):
        if self.current_room < self.total_room:
            self.current_room += 1
            print(f"Progression : Salle {self.current_room}/{self.total_room}")
        else:
            print("Vous êtes devant la salle du Boss !")

    def can_acces(self, player):
        return True