# Fantasy RPG Terminal Game

Ein textbasiertes Fantasy-Rollenspiel, das im Terminal läuft, entwickelt in Python. Das Spiel bietet eine Vielzahl von Features, einschließlich Charakterentwicklung, Kämpfen, Inventar, Quests und einer interaktiven Welt. Dieses Projekt dient als Grundlage für ein komplexes, rundenbasiertes RPG, das leicht erweitert und angepasst werden kann.

## Features

- **Charakterentwicklung**: Wähle eine Rasse und Klasse, entwickle deinen Charakter, steige im Level auf und lerne neue Fähigkeiten.
- **Rundenbasierte Kämpfe**: Kämpfe gegen Feinde, nutze Zauber, Heiltränke und Waffen, um zu gewinnen.
- **Inventarsystem**: Sammle und verwende Items wie Heiltränke, Waffen und magische Artefakte.
- **Questsystem**: Nimm Quests an, erfülle Aufgaben und erhalte Belohnungen wie Erfahrung, Gold und Items.
- **Kommandozeilen-Interface**: Alles läuft im Terminal, was den klassischen Charme eines RPGs bietet.

## Projektstruktur

Das Projekt ist in mehrere Module unterteilt, die jeweils für einen bestimmten Teil des Spiels verantwortlich sind:

- `character.py`: Definiert die Charakterklasse, die Attribute und Methoden zur Interaktion mit dem Charakter.
- `combat.py`: Enthält die Logik für das rundenbasierte Kampfsystem.
- `inventory.py`: Verwaltert das Inventarsystem, mit dem der Spieler Items sammeln und verwenden kann.
- `quests.py`: Implementiert das Quest-System, mit dem der Spieler Quests annehmen und abschließen kann.
- `game.py`: Der Hauptcode, der die Spiellogik steuert, Quests zuweist, Kämpfe durchführt und den Spielverlauf steuert.

## Anforderungen

- Python 3.x
- Keine externen Bibliotheken

