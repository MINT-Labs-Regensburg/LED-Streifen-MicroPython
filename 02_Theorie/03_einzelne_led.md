# Einzelne LED Grundlagen

In diesem Kapitel lernst du die Grundlagen zur Ansteuerung einer einzelnen LED mit einem Mikrocontroller und MicroPython.

## Was ist eine LED?
Eine LED (Licht emittierende Diode) ist ein elektronisches Bauteil, das Licht aussendet, wenn Strom hindurchfließt.

## Schaltplan
Um eine LED sicher zu betreiben, benötigt man einen Vorwiderstand. Der Schaltplan sieht folgendermaßen aus:

- Mikrocontroller Pin → Vorwiderstand → LED → Masse (GND)

## MicroPython Beispiel
```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)  # Pin 2 als Ausgang definieren

while True:
    led.value(1)  # LED einschalten
    time.sleep(1)
    led.value(0)  # LED ausschalten
    time.sleep(1)
```

## Aufgaben
1. Baue die Schaltung auf dem Steckbrett nach.
2. Übertrage das Beispielprogramm auf den Mikrocontroller.
3. Beobachte das Blinken der LED.

## Fragen
- Warum ist ein Vorwiderstand notwendig?
- Was passiert, wenn du die LED direkt ohne Widerstand anschließt?

---

Weiterführende Informationen findest du im Kapitel `einzelne_led_basics.md`.
