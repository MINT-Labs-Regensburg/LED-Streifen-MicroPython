"""
Beispiel 1: LED-Streifen Grundlagen
===================================

Erste Schritte mit LED-Streifen am Raspberry Pi Pico.

Hardware: LED-Streifen an Pin GP16

Gemeinsam machen!
"""

import time
import machine
from neopixel import NeoPixel

# Setup
pin = machine.Pin(16, machine.Pin.OUT)
leds = NeoPixel(pin, 10)  # 10 LEDs

print("LED-Streifen bereit!")

# Farben
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
AUS = (0, 0, 0)

# Erste LED rot machen
leds[0] = ROT
leds.write()  # Wichtig!
time.sleep(2)

# Erste LED grün machen
leds[0] = GRUEN
leds.write()
time.sleep(2)

# Erste LED blau machen
leds[0] = BLAU
leds.write()
time.sleep(2)

# LED ausschalten
leds[0] = AUS
leds.write()

print("Fertig!")
