"""
ALLE AUFGABEN: LED-Streifen Programmierung
Raspberry Pi Pico + WS2812B LED-Streifen

"""

# ==============================================
# IMPORTS UND SETUP (für alle Aufgaben)
# ==============================================

import machine
import time
from neopixel import NeoPixel

# Einzelne LED Setup (für Aufgabe 1)
einzelne_led = machine.Pin(25, machine.Pin.OUT)  # 25 oder 16 oder ...

# LED-Streifen Setup
LED_GP = 16  # oder 25 oder ...
ANZAHL_LEDS = 10
pin = machine.Pin(LED_GP, machine.Pin.OUT)
leds = NeoPixel(pin, ANZAHL_LEDS)

# ==============================================
# AUFGABE 1: Einzelne LED - SOS Signal
# ==============================================
"""
Programmiere ein SOS-Signal mit der einzelnen LED:
- 3x kurz blinken (S)
- 3x lang blinken (O)
- 3x kurz blinken (S)
- 2 Sekunden Pause
- Wiederhole das ganze 5 mal

Tipp: Kurz = 0.2 Sekunden, Lang = 0.8 Sekunden
"""

# ==============================================
# AUFGABE 2: LED-Streifen - Ampelschaltung
# ==============================================
"""
Erstelle eine Ampelschaltung:
- Erste LED rot für 3 Sekunden
- Erste LED gelb für 1 Sekunde  
- Erste LED grün für 3 Sekunden
- Wiederhole endlos

Erweitere es: Zeige alle drei Farben gleichzeitig auf LED 1, 2, 3
"""

# ==============================================
# AUFGABE 3: Lauflicht - Ping Pong
# ==============================================
"""
Programmiere ein "Ping Pong" Lauflicht:
- Eine LED läuft von links nach rechts
- Am Ende angekommen läuft sie zurück von rechts nach links
- Das wiederholt sich endlos
- Verwende eine schöne Farbe deiner Wahl

Tipp: Du brauchst zwei Schleifen - eine vorwärts, eine rückwärts
"""

# ==============================================
# AUFGABE 4: Regenbogen - Pulsierende Helligkeit
# ==============================================
"""
Erstelle einen pulsierenden Regenbogen:
- Zeige alle Regenbogenfarben auf dem LED-Streifen
- Die Helligkeit soll langsam hoch und runter gehen
- Wie ein "atmender" Regenbogen

Tipp: Du musst die RGB-Werte mit einem Faktor multiplizieren
der zwischen 0.1 und 1.0 wechselt
"""
