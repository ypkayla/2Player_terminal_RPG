class Item:
    def __init__(self, name, typ, staerke=0, magie=0, heilung=0):
        self.name = name
        self.typ = typ
        self.staerke = staerke
        self.magie = magie
        self.heilung = heilung

    def __str__(self):
        return f"{self.name} ({self.typ})"

class Inventar:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item {item} zum Inventar hinzugefügt.")

    def anzeigen(self):
        if not self.items:
            print("Das Inventar ist leer.")
        for item in self.items:
            print(item)

    def verwenden(self, item_name, charakter):
        for item in self.items:
            if item.name == item_name:
                if item.typ == "Heiltrank":
                    charakter.leben += item.heilung
                    print(f"{charakter.name} benutzt {item.name} und heilt sich um {item.heilung} Lebenspunkte.")
                    self.items.remove(item)
                elif item.typ == "Waffe":
                    charakter.staerke += item.staerke
                    print(f"{charakter.name} benutzt {item.name} und seine Stärke steigt um {item.staerke}.")
                    self.items.remove(item)
                elif item.typ == "Magie":
                    charakter.magie += item.magie
                    print(f"{charakter.name} benutzt {item.name} und seine Magie steigt um {item.magie}.")
                    self.items.remove(item)
                break
