# LED-Streifen Python Programmierung mit Raspberry Pi Pico

## 💝 Herzlichen Dank

| Ein herzliches Dankeschön an **Dr. Norwin von Malm** und **Stefan Grötsch** – die Preisträger des [Deutschen Zukunftspreises 2024](https://www.deutscher-zukunftspreis.de/de/team-1-2024).<br><br>Mit ihrer Spende und ihrer großzügigen Unterstützung haben Sie die Entwicklung und Durchführung dieses Kurses ermöglicht. 🙏 | <img src="assets/DZP_Logo_2.svg" alt="DZP Logo" width="120"/> |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: |

---

## Kurs-Übersicht
**Zielgruppe**: Schüler\*innen  
**Dauer**: 3 Stunden  
**Editor**: **Thonny IDE** (benutzerfreundlichster Python-Editor)  
**Hardware**: Raspberry Pi Pico + USB Kabel + WS2812B LED-Streifen + Einzel LED mit Widerstand

## Lernziele
- Raspberry Pi Pico verstehen und verwenden
- LED-Streifen anschließen und programmieren
- Python-Code für Hardware schreiben
- Eigene LED-Animationen entwickeln

## Vorbereitung durch Kursleitung (vor dem Kurs)

### `01_Setup/` - Hardware & Software-Vorbereitung
- [**`software_installation.md`**](01_Setup/software_installation.md) - Thonny-Setup (PC) und MicroPython (Pi Pico) installieren

## Ausdrucken Kursunterlagen

Diese Materialien sollten für die Schüler\*innen ausgedruckt werden:

- [**`aufgabe_alle.py`**](04_Aufgaben/aufgabe_alle.py) - Alle Programmieraufgaben in einer Datei
- [**`python-cheat-sheet.pdf`**](assets/python-cheat-sheet.pdf) - Python Kurzübersicht zum Nachschlagen
- [**`raspberry-pi-pico-gpio.png`**](assets/raspberry-pi-pico-gpio.png) - GPIO Pin-Belegung des Raspberry Pi Pico

## Kursdurchführung

### `02_Theorie/` - Kompakte Grundlagen (15 Min)
- [**`mikrocontroller_grundlagen.md`**](02_Theorie/01_mikrocontroller_grundlagen.md) - Raspberry Pi Pico Basics
- [**`einzelne_led_grundlagen.md`**](02_Theorie/03_einzelne_led_grundlagen.md) - Einzelne LED Grundlagen
- [**`led_streifen_grundlagen.md`**](02_Theorie/04_led_streifen_grundlagen.md) - LED-Technik kompakt

### `03_Python Grundlagen/` - Programmierung in Python

Für eine Python-Einführung siehe unseren separaten Kurs **[PYTHON-PYGAME](https://github.com/MINT-Labs-Regensburg/PYTHON-PYGAME)** 

In **Teil 2: Python - Listen, Schleifen & Co.** findest du Übungen zu
- **Variablen** - Daten speichern und verwenden
- **If Statements** - Deinem Programm Entscheidungen beibringen
- **Schleifen** - Lass den Computer für dich arbeiten!

Eine Kürzübersicht zu Python ist hier **[Python Cheat Sheet](assets/python-cheat-sheet.pdf)**

### `04_Aufgaben/` - Live-Programming LED Streifen

Diese Programmieraufgaben werden während des Kurses gemeinsam gelöst:

- [**`aufgabe01.py`**](04_Aufgaben/aufgabe01.py) - SOS Signal mit einzelner LED
- [**`aufgabe02.py`**](04_Aufgaben/aufgabe02.py) - Ampelschaltung mit LED-Streifen
- [**`aufgabe03.py`**](04_Aufgaben/aufgabe03.py) - Ping Pong Lauflicht
- [**`aufgabe04.py`**](04_Aufgaben/aufgabe04.py) - Pulsierender Regenbogen

Jede Aufgabe wird live im Kurs programmiert.

## Benötigte Hardware

### Für jede\*n Schüler\*in:
Dieses Material können die Schüler\*innen mit nach Hause nehmen
- 1x Raspberry Pi Pico H mit Header Pins (Mit von uns vorinstalliertem MicroPython)
- 1x LED + 220 Ohm Widerstand + Jumper Kabeln (weiblich rot, blau) von uns vorbereitet
- 1x WS2812B LED-Streifen (10 LEDs) mit drei Anschluss-Jumperkabeln (weiblich rot, blau, gelb) von uns vorbereitet
- 1x USB-A zu USB-C Kabel

Die Schüler\*innen benötigen zu Hause einen Computer mit Internetzugriff um darauf Thonny zu installieren. (Windows, Mac, Linux)

## Mehr Projekte und Anleitungen findest du [hier](https://wiki.mint-labs.de/)
