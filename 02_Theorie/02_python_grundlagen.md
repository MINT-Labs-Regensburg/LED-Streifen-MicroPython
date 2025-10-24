# 🐍 Python-Grundlagen für LED-Programmierung

*Für Kursleiter\*innen: Diese Datei enthält die wichtigsten Python-Konzepte für den Kurs. Detaillierte Erklärungen erfolgen während der Kursanleitung.*

## Warum MicroPython?
**MicroPython** ist eine vereinfachte Python-Version für Mikrocontroller wie den **Raspberry Pi Pico**. Gleiche Befehle wie "normales" Python, aber optimiert für Hardware-Steuerung.

## 📝 Wichtige Python-Konzepte

### 1. Variablen und Listen
```python
# Variablen
led_anzahl = 10
geschwindigkeit = 0.5
farbe_name = "rot"

# Listen (für mehrere Werte)
farben = ["rot", "grün", "blau"]
rgb_rot = [255, 0, 0]
```

### 2. Schleifen
```python
# For-Schleife (bestimmte Anzahl)
for i in range(5):
    print(f"Durchgang {i}")

# While-Schleife (mit Bedingung)
zaehler = 0
while zaehler < 3:
    zaehler = zaehler + 1
```

### 3. Funktionen
```python
def led_rot_machen(led_nummer):
    """Macht eine LED rot"""
    leds[led_nummer] = (255, 0, 0)
    leds.write()
```

## 🔌 Hardware-Programmierung

### Standard-Setup für Raspberry Pi Pico
```python
# Module importieren
import time
import machine
from neopixel import NeoPixel

# Hardware konfigurieren
LED_GP = 16  # GPIO16 für LED-Streifen
ANZAHL_LEDS = 10
pin = machine.Pin(LED_GP, machine.Pin.OUT)
leds = NeoPixel(pin, ANZAHL_LEDS)

# Farben definieren
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
```

### LED-Steuerung
```python
# Einzelne LED setzen
leds[0] = ROT           # LED 0 rot
leds[1] = GRUEN         # LED 1 grün
leds.write()            # WICHTIG: Änderungen anzeigen!

# Alle LEDs auf einmal
for i in range(10):
    leds[i] = BLAU
leds.write()
```

## 🚨 Häufige Fehler

### 1. `write()` vergessen
```python
# ❌ Falsch - LEDs ändern sich nicht
leds[0] = (255, 0, 0)

# ✅ Richtig
leds[0] = (255, 0, 0)
leds.write()  # Dieser Befehl ist Pflicht!
```

### 2. Falsche LED-Nummern
```python
# Bei 10 LEDs: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
leds[10] = (255, 0, 0)  # ❌ FEHLER! LED 10 existiert nicht
leds[9] = (255, 0, 0)   # ✅ Richtig - letzte LED
```

### 3. Endlosschleife ohne Pause
```python
# ❌ Falsch - Programm blockiert
while True:
    leds[0] = (255, 0, 0)

# ✅ Richtig - mit Pause
while True:
    leds[0] = (255, 0, 0)
    leds.write()
    time.sleep(0.1)  # Kurze Pause
```

## 🎯 Programmstruktur-Vorlage
```python
# 1. IMPORTS
import time, machine
from neopixel import NeoPixel

# 2. HARDWARE SETUP
LED_GP = 16
leds = NeoPixel(machine.Pin(LED_GP, machine.Pin.OUT), 10)

# 3. FARBEN
ROT = (255, 0, 0)

# 4. HAUPTPROGRAMM
def main():
    leds[0] = ROT
    leds.write()
    time.sleep(1)

# 5. PROGRAMM STARTEN
main()
```

## 💡 Kursleiter\*innen-Hinweise
- **Hands-on zuerst**: Direkt mit LEDs experimentieren, Theorie parallel erklären
- **Live-Coding**: Gemeinsam Code entwickeln, Fehler bewusst machen und korrigieren
- **Pin-Nummern beachten**: GP16 für LED-Streifen oder GP16 für einzelne LEDs
- **Debugging**: `print()`-Befehle nutzen, schrittweise testen

*Die detaillierten Erklärungen und Übungen werden während des Kurses interaktiv durchgeführt.*
