# LED-Beispiel 4: Regenbogen
# Alle LEDs zeigen verschiedene Regenbogenfarben

import time
import machine
from neopixel import NeoPixel

# Hardware Setup
pin = machine.Pin(16, machine.Pin.OUT)
leds = NeoPixel(pin, 10)

print("Regenbogen startet...")

# Regenbogenfarben (10 Farben für 10 LEDs)
regenbogen = [
    (255, 0, 0),  # Rot
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Gelb
    (127, 255, 0),  # Gelbgrün
    (0, 255, 0),  # Grün
    (0, 255, 127),  # Blaugrün
    (0, 255, 255),  # Cyan
    (0, 127, 255),  # Hellblau
    (0, 0, 255),  # Blau
    (127, 0, 255),  # Violett
]

# Endlos-Schleife
while True:
    # Regenbogen anzeigen
    for i in range(10):
        leds[i] = regenbogen[i]
    leds.write()
    time.sleep(2)

    # Regenbogen rotieren
    for rotation in range(10):
        for i in range(10):
            # Index mit Rotation berechnen
            farb_index = (i + rotation) % 10
            leds[i] = regenbogen[farb_index]
        leds.write()
        time.sleep(0.3)
