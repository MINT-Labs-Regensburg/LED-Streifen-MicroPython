# Streifen-LED-Beispiel 2: Farben wechseln
# Zeigt verschiedene Grundfarben nacheinander

import time
import machine
from neopixel import NeoPixel

# Hardware Setup
pin = machine.Pin(16, machine.Pin.OUT)
leds = NeoPixel(pin, 10)

print("Farben-Wechsel startet...")

# Farben definieren (R, G, B)
farben = [
    (255, 0, 0),  # Rot
    (0, 255, 0),  # Grün
    (0, 0, 255),  # Blau
    (255, 255, 0),  # Gelb
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 255, 255),  # Weiß
]

# Endlos-Schleife
while True:
    for farbe in farben:
        # Erste LED mit aktueller Farbe
        leds[0] = farbe
        leds.write()
        time.sleep(1)

    # Kurze Pause zwischen Durchläufen
    leds[0] = (0, 0, 0)  # LED aus
    leds.write()
    time.sleep(0.5)
