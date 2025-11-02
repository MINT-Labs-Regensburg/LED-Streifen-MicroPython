"""
AUFGABE 2: LED-Streifen - Ampelschaltung

Erstelle eine Ampelschaltung:
- Erste LED rot für 3 Sekunden
- Erste LED gelb für 1 Sekunde
- Erste LED grün für 3 Sekunden
- Wiederhole endlos

Erweitere es: Zeige alle drei Farben gleichzeitig auf LED 1, 2, 3
"""


# HINWEIS: 
# Damit du die LED-Streifen ansteuern kannst, musst du machine und NeoPixel importieren
# LED_GP: An diesen GP Port ist die Datenleitung des LED-Streifens angeschlossen
# ANZAHL_LEDS: Soviel LEDS sind auf deinem LED Streifen
import machine
from neopixel import NeoPixel

LED_GP = 16  # GPIO16 für Datenleitung
ANZAHL_LEDS = 10  # Standard-Streifenlänge
pin = machine.Pin(LED_GP, machine.Pin.OUT)
leds = NeoPixel(pin, ANZAHL_LEDS)
