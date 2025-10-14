# 💻 Thonny Setup für Raspberry Pi Pico

> **Ziel:** Python-Editor für LED-Programmierung einrichten

---

## 🚀 **Schritt 1:** Thonny am PC installieren

### 📥 Download & Installation

1. **Website besuchen:** [thonny.org](https://thonny.org)
2. **Windows-Version herunterladen:** `thonny-4.x.x.exe`
3. **Installation starten:** Rechtsklick → "Als Administrator ausführen"
4. **Installieren:** Alle Standard-Einstellungen übernehmen

✅ **Ergebnis:** Thonny ist auf dem PC installiert

---

## 📥 **Schritt 2:** MicroPython auf Pico installieren

### 🔌 Pico im BOOTSEL-Modus starten

1. **BOOTSEL-Taste** am Pico **gedrückt halten**
2. **USB-Kabel** anschließen (Taste weiter gedrückt halten)
3. **Taste loslassen** → Pico erscheint als USB-Laufwerk `"RPI-RP2"`
4. **Thonny öffnen** (falls noch nicht geöffnet)

### ⚡ MicroPython flashen

1. **Menü:** `Ausführen` → `Konfigurieren des Interpreters...`
2. **Button:** `"MicroPython installieren oder aktualisieren"` rechts unten anklicken
3. **Target Volume:** `"RPI-RP2"` auswählen
4. **MicroPython Family:** `"RP2"` auswählen
5. **Gerät/variant:** `"Raspberry Pi Pico"` auswählen
6. **Installation starten:** `"Install"` klicken

> ⏱️ **Hinweis:** Installation dauert ~1 Minute. Warten bis `"Done!"` erscheint.

### 🔄 Pico und Thonny neu starten

1. **Pico trennen:** USB-Kabel abziehen und wieder anschließen
2. **Thonny neu starten:** Programm schließen und erneut öffnen

✅ **Ergebnis:** MicroPython ist auf dem Pico installiert

---

## ⚙️ **Schritt 3:** Thonny mit Pico verbinden

### 🎯 Interpreter einstellen

1. **Interpreter auswählen:** Unten rechts in Thonny `"MicroPython (Raspberry Pi Pico)"` und den passenden COM-Port auswählen  
   (z.B. `"MicroPython (Raspberry Pi Pico) Board CDC @COMXXX"`)

> ⚠️ **Wichtig:** Die Option `"MicroPython (Raspberry Pi Pico)"` erscheint nur, wenn MicroPython bereits auf dem Pico installiert ist.

✅ **Ergebnis:** Thonny ist mit dem Pico verbunden

### 🧪 Verbindung testen

**In der Thonny-Shell / Kommandozeile (unten) eingeben:**

```python
>>> print("Hello World vom Pico!")
```

✅ **Ergebnis:** Wenn "Hello World vom Pico!" erscheint, funktioniert die Verbindung

---

## 🎉 **Setup abgeschlossen!**

**Thonny ist jetzt bereit für den LED-Programmier-Kurs!** 🚀

---

## 🔌 Hardware-Hinweis

Die Anschlüsse für die Farb-LEDs (WS2812B) und die einzel LEDs sind vorbereitet, sodass ihr direkt mit dem Programmieren starten könnt.

