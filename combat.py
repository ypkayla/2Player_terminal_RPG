from character import Charakter
import random

def kampf(char1: Charakter, char2: Charakter):
    print(f"\nDer Kampf zwischen {char1.name} und {char2.name} beginnt!\n")
    
    while not char1.ist_tot() and not char2.ist_tot():
        char1.fähigkeit_auswahl(char2)
        
        if char2.ist_tot():
            print(f"{char2.name} ist gestorben! {char1.name} gewinnt den Kampf!")
            break
        
        char2.fähigkeit_auswahl(char1)
        
        if char1.ist_tot():
            print(f"{char1.name} ist gestorben! {char2.name} gewinnt den Kampf!")
            break

        print(f"\n{char1.name}: {char1.leben}/{char1.max_leben} Leben")
        print(f"{char2.name}: {char2.leben}/{char2.max_leben} Leben")
        input("Drücke Enter, um die nächste Runde zu starten.")
