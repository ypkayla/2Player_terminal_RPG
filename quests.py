class Quest:
    def __init__(self, titel, beschreibung, ziel, belohnung):
        self.titel = titel
        self.beschreibung = beschreibung
        self.ziel = ziel  # Ziel könnte etwas wie "Töte 5 Goblins" oder "Bringe 10 Gold" sein
        self.belohnung = belohnung  # Belohnung kann Erfahrungspunkte, Gold oder Items sein
        self.erledigt = False  # Wird auf True gesetzt, wenn die Quest abgeschlossen ist

    def check_quest_status(self, charakter):
        """Überprüft, ob das Ziel der Quest erreicht wurde."""
        if not self.erledigt:
            if self.ziel == "Töte 5 Goblins" and charakter.get_goblins_getoetet() >= 5:
                self.erledigt = True
                charakter.add_experience(50)
                charakter.gold += 100
                print(f"Quest '{self.titel}' abgeschlossen! {self.belohnung} erhalten.")
            elif self.ziel == "Bringe 10 Gold" and charakter.gold >= 10:
                self.erledigt = True
                charakter.add_experience(30)
                charakter.gold -= 10  # Abgabe der Goldmenge
                print(f"Quest '{self.titel}' abgeschlossen! {self.belohnung} erhalten.")

    def anzeigen(self):
        """Zeigt die Details der Quest an."""
        status = "Erledigt" if self.erledigt else "Offen"
        print(f"Quest: {self.titel}")
        print(f"Status: {status}")
        print(f"Beschreibung: {self.beschreibung}")
        print(f"Ziel: {self.ziel}")
        print(f"Belohnung: {self.belohnung}")


class Questgeber:
    def __init__(self, name):
        self.name = name
        self.quests = []

    def quest_angebot_hinzufuegen(self, quest):
        """Fügt dem Questgeber eine neue Quest hinzu."""
        self.quests.append(quest)

    def quest_angebot_anzeigen(self):
        """Zeigt alle verfügbaren Quests des Questgebers an."""
        print(f"\n{self.name} hat folgende Quests für dich:")
        for quest in self.quests:
            quest.anzeigen()

    def quest_annahme(self, quest_index):
        """Nimmt eine Quest an, basierend auf dem Index in der Liste der Quests."""
        if 0 <= quest_index < len(self.quests):
            quest = self.quests[quest_index]
            print(f"Du hast die Quest '{quest.titel}' angenommen.")
            return quest
        else:
            print("Ungültiger Quest-Index.")
            return None
