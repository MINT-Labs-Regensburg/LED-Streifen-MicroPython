"""
AUFGABE 2: LED-Streifen - Ampelschaltung

Erstelle eine Ampelschaltung:
- Erste LED rot für 3 Sekunden
- Erste LED gelb für 1 Sekunde
- Erste LED grün für 3 Sekunden
- Wiederhole endlos

Erweitere es: Zeige alle drei Farben gleichzeitig auf LED 1, 2, 3
"""

import machine
import time
from neopixel import NeoPixel

LED_GP = 16
ANZAHL_LEDS = 10
pin = machine.Pin(LED_GP, machine.Pin.OUT)
leds = NeoPixel(pin, ANZAHL_LEDS)

# Farben definieren
rot = (255, 0, 0)
gelb = (255, 255, 0)
gruen = (0, 255, 0)
aus = (0, 0, 0)

print("Ampel startet...")

# Endlos-Schleife für Ampel
while True:
    # Rot für 3 Sekunden
    leds[0] = rot
    leds.write()
    time.sleep(3)

    # Gelb für 1 Sekunde
    leds[0] = gelb
    leds.write()
    time.sleep(1)

    # Grün für 3 Sekunden
    leds[0] = gruen
    leds.write()
    time.sleep(3)
