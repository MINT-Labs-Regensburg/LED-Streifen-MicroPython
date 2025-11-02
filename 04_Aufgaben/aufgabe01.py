"""
AUFGABE 1: Einzelne LED - SOS Signal

Lass zuerst die externe Einzel LED blinken. Dann die eingebaute LED

Programmiere ein SOS-Signal mit der einzelnen LED:
- 3x kurz blinken (S)
- 3x lang blinken (O)
- 3x kurz blinken (S)
- 2 Sekunden Pause
- Wiederhole das ganze 5 mal

Tipp: Kurz = 0.2 Sekunden, Lang = 0.8 Sekunden
"""

import machine
import time

# LED anschließen
led = machine.Pin(16, machine.Pin.OUT)

# SOS Signal 5 mal
for runde in range(5):
    print(f"SOS {runde+1}")

    # S - 3x kurz
    for i in range(3):
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    # O - 3x lang
    for i in range(3):
        led.value(1)
        time.sleep(0.8)
        led.value(0)
        time.sleep(0.2)

    # S - 3x kurz
    for i in range(3):
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    # Pause zwischen SOS
    time.sleep(2)

print("Fertig!")
