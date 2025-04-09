from character import Charakter
from combat import kampf
from inventory import Item, Inventar

def main():
    # Initialisierung der Charaktere
    char1 = Charakter(name="Aragorn", rasse="Mensch", klasse="Krieger", leben=100, staerke=20, geschicklichkeit=15, intelligenz=10, magie=5)
    char2 = Charakter(name="Gandalf", rasse="Zauberer", klasse="Magier", leben=80, staerke=10, geschicklichkeit=10, intelligenz=20, magie=30)

    # Initialisierung des Inventars
    inventar1 = Inventar()
    inventar2 = Inventar()

    # Füge Items hinzu
    heiltrank = Item(name="Heiltrank", typ="Heiltrank", heilung=20)
    schwert = Item(name="Schwert", typ="Waffe", staerke=10)
    zauberbuch = Item(name="Zauberbuch", typ="Magie", magie=15)

    inventar1.add_item(heiltrank)
    inventar2.add_item(zauberbuch)
    inventar1.add_item(schwert)

    # Kampf starten
    kampf(char1, char2)

if __name__ == "__main__":
    main()
