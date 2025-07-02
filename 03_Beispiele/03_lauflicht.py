# LED-Beispiel 3: Lauflicht
# Eine LED wandert durch den Streifen

import time
import machine
from neopixel import NeoPixel

# Hardware Setup
pin = machine.Pin(16, machine.Pin.OUT)
leds = NeoPixel(pin, 10)

print("Lauflicht startet...")

# Farbe für das Lauflicht
farbe = (0, 255, 0)  # Grün

# Endlos-Schleife
while True:
    # Vorwärts: LED 0 bis 9
    for i in range(10):
        # Alle LEDs aus
        for j in range(10):
            leds[j] = (0, 0, 0)

        # Aktuelle LED an
        leds[i] = farbe
        leds.write()
        time.sleep(0.2)

    # Rückwärts: LED 9 bis 0
    for i in range(8, -1, -1):
        # Alle LEDs aus
        for j in range(10):
            leds[j] = (0, 0, 0)

        # Aktuelle LED an
        leds[i] = farbe
        leds.write()
        time.sleep(0.2)
