"""
💡 Beispiel 0: Einzelne LED (Einstieg)
=============================

Einfachste LED-Steuerung - LED blinkt 10x.

🔧 Hardware:
   • Nur Raspberry Pi Pico (keine extra LED nötig!)
   • Interne LED: Kleine LED auf dem Pico-Board

🔌 Alternative - Externe LED:
   • GPIO-Pin (GP16) → Widerstand 220-470Ω → LED → GND

👨‍🏫 Gemeinsam durchgehen!
"""

import time
import machine


# Interne LED konfigurieren (Pin 25)
led = machine.Pin(25, machine.Pin.OUT)

# Alternative: Externe LED an Pin 16 verwenden
# led = machine.Pin(16, machine.Pin.OUT)  # GP16 → Widerstand 220 bis 470 Ohm → LED → GND

# 10x blinken
for i in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    print(f"Blink {i+1}/10")

led.on()
print("Fertig!")
