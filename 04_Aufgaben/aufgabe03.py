"""
AUFGABE 3: Lauflicht - Ping Pong

Programmiere ein "Ping Pong" Lauflicht:
- Eine LED läuft von links nach rechts
- Am Ende angekommen läuft sie zurück von rechts nach links
- Das wiederholt sich endlos
- Verwende eine schöne Farbe deiner Wahl

Tipp: Du brauchst zwei Schleifen - eine vorwärts, eine rückwärts
"""

import machine
import time
from neopixel import NeoPixel

LED_GP = 16
ANZAHL_LEDS = 10
pin = machine.Pin(LED_GP, machine.Pin.OUT)
leds = NeoPixel(pin, ANZAHL_LEDS)

# Farbe wählen
meine_farbe = (0, 100, 255)  # Blau
aus = (0, 0, 0)

print("Ping Pong Lauflicht startet...")

while True:
    # Von links nach rechts (0 bis 9)
    for i in range(ANZAHL_LEDS):
        # Alle LEDs aus
        for j in range(ANZAHL_LEDS):
            leds[j] = aus

        # Aktuelle LED an
        leds[i] = meine_farbe
        leds.write()
        time.sleep(0.1)

    # Von rechts nach links (9 bis 0)
    for i in range(ANZAHL_LEDS - 1, -1, -1):
        # Alle LEDs aus
        for j in range(ANZAHL_LEDS):
            leds[j] = aus

        # Aktuelle LED an
        leds[i] = meine_farbe
        leds.write()
        time.sleep(0.1)
