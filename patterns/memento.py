import json

from copy import deepcopy
from models.items import Item, Potion, Antidote, Bombe, Arme, Armure, ClefDuDonjon


class Originator:

    def __init__(self, player):
        self.player = player
        self._state = list(player.inventory)

    def set_state(self, state):
        self._state = state

    def save_to_memento(self):
        serialized = self._serialize_inventory(self.player.inventory)

        filename = f"save/{self.player.name}_inventory.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(serialized, f, ensure_ascii=False, indent=2)
        return Originator.Memento(deepcopy(serialized))

    def restore_from_memento(self, memento):
        state = memento.get_saved_state()
        deserialized = self._deserialize_inventory(state)
        self.player.inventory = deserialized
        self._state = list(deserialized)

    def _serialize_inventory(self, inventory):
        serialized = []
        for item in inventory:
            d = {"class": item.__class__.__name__, "name": item.name, "consommable": item.consommable}
            serialized.append(d)
        return serialized

    def _deserialize_inventory(self, state):
        items = []
        for d in state:
            cls = d.get("class")
            if cls == "ClefDuDonjon":
                item = ClefDuDonjon(d.get("name", "Clé du Donjon"), d.get("consommable", False))
            else:
                item = Item(d.get("name", "item"), d.get("consommable", False))
            items.append(item)
        return items

    class Memento:
        def __init__(self, state):
            self._state = state

        def get_saved_state(self):
            return self._state

class Caretaker:
    def __init__(self, originator):
        self.originator = originator
        self.saved_states = []

    def save_state(self):
        print("Sauvegarde ...")
        self.saved_states.append(self.originator.save_to_memento())

