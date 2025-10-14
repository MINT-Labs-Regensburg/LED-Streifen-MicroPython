

# 💡 Einzel-LED Grundlagen

*Für Kursleiter\*innen: Essentielles Wissen zur einzelnen LED. Praktische Details werden im Kurs live erklärt.*

## Was ist eine LED?
Eine **LED** (Licht-Emittierende Diode) ist ein elektronisches Bauteil, das Licht abgibt, wenn Strom hindurchfließt. Sie ist sehr effizient und in vielen Farben erhältlich.

### Vorteile für den Kurs:
- **Sehr einfach**: Nur 2 Anschlüsse (Plus/Minus)
- **Sicher**: Geringe Spannung, keine Verletzungsgefahr
- **Sofort sichtbarer Effekt**: Erfolgserlebnis garantiert

## 🔌 Anschluss einer LED am Raspberry Pi Pico

### Benötigte Bauteile:
- 1x LED (z.B. rot)
- 1x 220 Ohm Widerstand (Schutz für die LED)
- 2x Jumper-Kabel

### Schaltskizze:
```
LED (+) Anode  → Widerstand → GP16 (Pico)
LED (-) Kathode → GND (Pico)
```
![Einzel-LED Schaltung](../assets/single_led.jpg)
### Merksatz für LED: Kurz, Kathode, Kante

- **Kurz**: Das kürzere Bein der LED ist die **Kathode** (Minuspol).
- **Kante**: Manche LEDs haben eine kleine **Kante** oder Abflachung am Gehäuse – diese zeigt zur Kathode.
### Beispiel-Foto: Einzelne LED am Raspberry Pi Pico

![Einzelne LED am Raspberry Pi Pico angeschlossen](../assets/single_led_pico.jpg)

> 💡 **Hinweis:** Falls Jumperkabel verlötet werden sollen, achtet darauf, dass sie Kupfer-Litzen besitzen. Günstige Jumperkabel bestehen oft aus CCA (Copper Clad Aluminum) und lassen sich schlecht löten.



*Das Foto zeigt eine einzelne LED mit Widerstand, verbunden mit dem Raspberry Pi Pico. Die Anode ist über den Widerstand an GP16 angeschlossen, die Kathode an GND.*

## 📝 Beispiel-Code
```python
import machine
import time

led = machine.Pin(16, machine.Pin.OUT)

# LED blinken lassen
for i in range(10):
    led.value(1)  # AN
    time.sleep(0.5)
    led.value(0)  # AUS
    time.sleep(0.5)
```

## ⚠️ Häufige Fehler
- LED falsch herum eingesteckt (Anode/Kathode vertauscht)
- Widerstand vergessen (LED wird zu heiß)
- Falscher Pin im Code

## 🎯 Lernziele
- Schaltplan lesen und umsetzen
- GPIO Pin ansteuern
- Zeitsteuerung mit `time.sleep()`

---
