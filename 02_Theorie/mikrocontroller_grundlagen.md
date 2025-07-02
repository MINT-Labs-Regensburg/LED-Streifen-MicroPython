# 🖥️ Mikrocontroller-Grundlagen

*Für Kursleiter*innen: Grundlegende Konzepte für den Einstieg. Details werden während der praktischen Übungen erklärt.*

## Was ist ein Mikrocontroller?
Ein **Mikrocontroller** ist ein kleiner Computer, der elektronische Geräte steuert - das "Gehirn" für unsere LED-Streifen.

## Der Raspberry Pi Pico

### Vorteile für den Kurs:
- **Einfach**: Plug & Play, keine Treiber
- **Günstig**: Nur ~4 Euro
- **Robust**: Wenig Hardware-Probleme
- **Bildungsfokus**: Speziell für Lernende entwickelt
- **Python-Support**: Mit MicroPython programmierbar

### Wichtige technische Daten:
```
Prozessor: Dual-Core ARM Cortex-M0+ (125 MHz)
Speicher: 264 KB RAM 
GPIO-Pins: 26 Anschlüsse
Stromversorgung: 3,3V (5V-tolerant)
USB: Direkte Verbindung
```

## 🔌 GPIO-Pins (Anschlüsse)

**GPIO** = General Purpose Input/Output

### Wichtige Pins für LED-Projekte:
```
GP16   → LED-Streifen (Datenleitung)
GP2    → Einzelne LED (zum Testen)
GND    → Minus-Pol (Erdung)
3V3    → 3,3V Stromversorgung
VSYS   → 5V für LED-Streifen
```
