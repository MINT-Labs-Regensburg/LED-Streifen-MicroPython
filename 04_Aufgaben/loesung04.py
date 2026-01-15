"""
AUFGABE 4: Regenbogen - Pulsierende Helligkeit

Erstelle einen pulsierenden Regenbogen:
- Zeige alle Regenbogenfarben auf dem LED-Streifen
- Die Helligkeit soll langsam hoch und runter gehen
- Wie ein "atmender" Regenbogen

Tipp: Du musst die RGB-Werte mit einem Faktor multiplizieren
der zwischen 0.1 und 1.0 wechselt
"""

import machine
import time
from neopixel import NeoPixel

LED_GP = 16
ANZAHL_LEDS = 10
pin = machine.Pin(LED_GP, machine.Pin.OUT)
leds = NeoPixel(pin, ANZAHL_LEDS)

# Regenbogenfarben
regenbogen = [
    (255, 0, 0),  # Rot
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Gelb
    (0, 255, 0),  # Grün
    (0, 0, 255),  # Blau
    (75, 0, 130),  # Indigo
    (148, 0, 211),  # Violett
    (255, 0, 255),  # Magenta
    (255, 100, 100),  # Rosa
    (100, 255, 255),  # Cyan
]

print("Pulsierender Regenbogen startet...")

helligkeit = 0.1
richtung = 0.05  # Schrittweite

while True:
    # Helligkeit ändern
    helligkeit += richtung

    # Richtung umkehren wenn Grenzen erreicht
    if helligkeit >= 1.0:
        richtung = -0.05
    elif helligkeit <= 0.1:
        richtung = 0.05

    # Jede LED mit Regenbogenfarbe und Helligkeit
    for i in range(ANZAHL_LEDS):
        farbe = regenbogen[i]

        # Farbe mit Helligkeit multiplizieren
        rot = int(farbe[0] * helligkeit)
        gruen = int(farbe[1] * helligkeit)
        blau = int(farbe[2] * helligkeit)

        leds[i] = (rot, gruen, blau)

    leds.write()
    time.sleep(0.1)
