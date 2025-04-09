import random

class Charakter:
    def __init__(self, name, rasse, klasse, leben, staerke, geschicklichkeit, intelligenz, magie, gold=0):
        self.name = name
        self.rasse = rasse
        self.klasse = klasse
        self.leben = leben
        self.staerke = staerke
        self.geschicklichkeit = geschicklichkeit
        self.intelligenz = intelligenz
        self.magie = magie
        self.gold = gold
        self.inventory = []
        self.level = 1
        self.experience = 0
        self.max_leben = leben

    def level_up(self):
        self.level += 1
        self.max_leben += 10
        self.leben = self.max_leben
        self.staerke += 2
        self.geschicklichkeit += 1
        self.intelligenz += 1
        print(f"{self.name} hat Level {self.level} erreicht!")

    def add_experience(self, amount):
        self.experience += amount
        print(f"{self.name} hat {amount} Erfahrungspunkte erhalten!")
        if self.experience >= 100:
            self.level_up()
            self.experience = 0

    def ist_tot(self):
        return self.leben <= 0

    def angreifen(self, gegner):
        schaden = random.randint(self.staerke // 2, self.staerke)
        gegner.leben -= schaden
        print(f"{self.name} greift {gegner.name} an und verursacht {schaden} Schaden!")

    def zaubern(self, gegner):
        schaden = random.randint(self.magie // 2, self.magie)
        gegner.leben -= schaden
        print(f"{self.name} zaubert und verursacht {schaden} magischen Schaden an {gegner.name}!")

    def heilen(self):
        heilung = random.randint(5, 15)
        self.leben += heilung
        if self.leben > self.max_leben:
            self.leben = self.max_leben
        print(f"{self.name} heilt sich um {heilung} Lebenspunkte.")

    def fähigkeit_auswahl(self, gegner):
        print("\nWähle eine Fähigkeit:")
        print("1. Angriff")
        print("2. Zauber")
        print("3. Heilen")
        wahl = input("Wähle 1, 2 oder 3: ")

        if wahl == "1":
            self.angreifen(gegner)
        elif wahl == "2":
            self.zaubern(gegner)
        elif wahl == "3":
            self.heilen()
        else:
            print("Ungültige Wahl.")
            self.fähigkeit_auswahl(gegner)
