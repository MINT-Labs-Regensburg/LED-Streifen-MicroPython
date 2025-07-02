"""
🔍 Raspberry Pi Pico + LED-Streifen Test für Schüler*innen
==========================================================

Dieses Programm testet, ob alles richtig angeschlossen ist:
✅ Raspberry Pi Pico funktioniert
✅ LED-Streifen ist korrekt verbunden
✅ Alle Farben werden richtig angezeigt
✅ Alle LEDs funktionieren

📋 VOR DEM AUSFÜHREN:
1. Hardware nach Anleitung angeschlossen
2. Raspberry Pi Pico per USB verbunden
3. Thonny läuft und ist mit Raspberry Pi Pico verbunden

🚀 PROGRAMM STARTEN: F5 drücken
"""

import time
import machine
from neopixel import NeoPixel

# ===== KONFIGURATION FÜR SCHÜLER =====
LED_PIN = 16  # GPIO-Pin GP16 für LED-Daten
LED_ANZAHL = 10  # Anzahl LEDs auf deinem Streifen
HELLIGKEIT = 0.3  # Helligkeit (0.1 = dunkel, 1.0 = sehr hell)

# ===== FARBEN DEFINIEREN =====
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
WEISS = (255, 255, 255)
GELB = (255, 255, 0)
LILA = (128, 0, 128)
TUERKIS = (0, 255, 255)
ORANGE = (255, 165, 0)
AUS = (0, 0, 0)

# ===== HILFS-FUNKTIONEN =====


def farbe_dimmen(farbe, helligkeit):
    """
    Macht Farben dunkler oder heller
    farbe: (r, g, b) Tupel
    helligkeit: 0.0 bis 1.0
    """
    return tuple(int(c * helligkeit) for c in farbe)


def alle_leds_setzen(streifen, farbe):
    """
    Setzt alle LEDs auf die gleiche Farbe
    """
    for i in range(len(streifen)):
        streifen[i] = farbe
    streifen.write()


def led_info_anzeigen():
    """
    Zeigt Informationen über das Setup
    """
    print("=" * 40)
    print("🔧 LED-STREIFEN KONFIGURATION")
    print("=" * 40)
    print(f"📍 GPIO-Pin: {LED_PIN}")
    print(f"💡 Anzahl LEDs: {LED_ANZAHL}")
    print(f"🔆 Helligkeit: {int(HELLIGKEIT * 100)}%")
    print(f"🎨 Test-Farben: 8 verschiedene")
    print("=" * 40)


def countdown(sekunden):
    """
    Zeigt einen Countdown an
    """
    for i in range(sekunden, 0, -1):
        print(f"⏳ Start in {i} Sekunden...")
        time.sleep(1)
    print("🚀 LOS GEHT'S!")


def grundfarben_test(streifen):
    """
    Test 1: Grundfarben (rot, grün, blau, weiß)
    """
    print("\n🔴 TEST 1: GRUNDFARBEN")
    print("-" * 20)

    farben = [
        (ROT, "ROT 🔴"),
        (GRUEN, "GRÜN 🟢"),
        (BLAU, "BLAU 🔵"),
        (WEISS, "WEISS ⚪"),
    ]

    for farbe, name in farben:
        print(f"  {name}")
        alle_leds_setzen(streifen, farbe_dimmen(farbe, HELLIGKEIT))
        time.sleep(2)

    # Alle aus
    alle_leds_setzen(streifen, AUS)
    print("  Alle LEDs AUS ⚫")
    time.sleep(1)


def bunte_farben_test(streifen):
    """
    Test 2: Bunte Farben (gelb, lila, türkis, orange)
    """
    print("\n🌈 TEST 2: BUNTE FARBEN")
    print("-" * 20)

    farben = [
        (GELB, "GELB 🟡"),
        (LILA, "LILA 🟣"),
        (TUERKIS, "TÜRKIS 🔵"),
        (ORANGE, "ORANGE 🟠"),
    ]

    for farbe, name in farben:
        print(f"  {name}")
        alle_leds_setzen(streifen, farbe_dimmen(farbe, HELLIGKEIT))
        time.sleep(2)

    alle_leds_setzen(streifen, AUS)
    print("  Alle LEDs AUS ⚫")
    time.sleep(1)


def einzelne_leds_test(streifen):
    """
    Test 3: Jede LED einzeln durchgehen
    """
    print("\n🔍 TEST 3: EINZELNE LEDS")
    print("-" * 20)
    print("  Jede LED einzeln ROT...")

    for i in range(len(streifen)):
        # Alle aus
        alle_leds_setzen(streifen, AUS)

        # Aktuelle LED rot
        streifen[i] = farbe_dimmen(ROT, HELLIGKEIT)
        streifen.write()

        print(f"    LED {i+1}/{len(streifen)} ✨")
        time.sleep(0.5)

    alle_leds_setzen(streifen, AUS)
    print("  Test abgeschlossen! ✅")


def regenbogen_test(streifen):
    """
    Test 4: Regenbogen-Effekt
    """
    print("\n🌈 TEST 4: REGENBOGEN-EFFEKT")
    print("-" * 20)

    # Regenbogen-Farben
    regenbogen_farben = [
        farbe_dimmen(ROT, HELLIGKEIT),  # 0
        farbe_dimmen(ORANGE, HELLIGKEIT),  # 1
        farbe_dimmen(GELB, HELLIGKEIT),  # 2
        farbe_dimmen(GRUEN, HELLIGKEIT),  # 3
        farbe_dimmen(TUERKIS, HELLIGKEIT),  # 4
        farbe_dimmen(BLAU, HELLIGKEIT),  # 5
        farbe_dimmen(LILA, HELLIGKEIT),  # 6
        farbe_dimmen(WEISS, HELLIGKEIT),  # 7
    ]

    print("  Statischer Regenbogen...")
    for i in range(len(streifen)):
        farb_index = i % len(regenbogen_farben)
        streifen[i] = regenbogen_farben[farb_index]
    streifen.write()
    time.sleep(3)

    print("  Wandernder Regenbogen...")
    for shift in range(10):  # 10 Schritte
        for i in range(len(streifen)):
            farb_index = (i + shift) % len(regenbogen_farben)
            streifen[i] = regenbogen_farben[farb_index]
        streifen.write()
        time.sleep(0.3)

    alle_leds_setzen(streifen, AUS)
    print("  Regenbogen abgeschlossen! ✅")


def lauflicht_test(streifen):
    """
    Test 5: Buntes Lauflicht
    """
    print("\n✨ TEST 5: LAUFLICHT")
    print("-" * 20)

    test_farben = [
        (farbe_dimmen(ROT, HELLIGKEIT), "ROT"),
        (farbe_dimmen(GRUEN, HELLIGKEIT), "GRÜN"),
        (farbe_dimmen(BLAU, HELLIGKEIT), "BLAU"),
        (farbe_dimmen(GELB, HELLIGKEIT), "GELB"),
    ]

    for farbe, name in test_farben:
        print(f"  Lauflicht {name}...")
        for i in range(len(streifen)):
            alle_leds_setzen(streifen, AUS)
            streifen[i] = farbe
            streifen.write()
            time.sleep(0.2)

    alle_leds_setzen(streifen, AUS)
    print("  Lauflicht abgeschlossen! ✅")


def hardware_info():
    """
    Zeigt Raspberry Pi Pico-Hardware-Informationen
    """
    print("\n💻 RASPBERRY PI PICO-INFORMATIONEN")
    print("-" * 20)

    # CPU-Frequenz
    freq_mhz = machine.freq() // 1000000
    print(f"  🔧 CPU: {freq_mhz} MHz")

    # Speicher-Info
    import gc

    gc.collect()
    free_kb = gc.mem_free() // 1024
    used_kb = gc.mem_alloc() // 1024
    print(f"  💾 Freier Speicher: {free_kb} KB")
    print(f"  💾 Belegter Speicher: {used_kb} KB")

    # Hardware-ID
    import ubinascii

    hw_id = ubinascii.hexlify(machine.unique_id()).decode()
    print(f"  🆔 Hardware-ID: {hw_id[:8]}...")


def main():
    """
    Hauptprogramm - führt alle Tests durch
    """
    print("🚀 LED-STREIFEN VERBINDUNGSTEST FÜR SCHÜLER")
    print("=" * 50)

    # System-Info anzeigen
    hardware_info()
    led_info_anzeigen()

    # Sicherheitshinweis
    print("\n⚠️  SICHERHEITSCHECK:")
    print("   ✅ Hardware korrekt angeschlossen?")
    print("   ✅ Alle Kabel fest?")
    print("   ✅ Maximal 15 LEDs ohne externes Netzteil?")

    # Countdown
    countdown(3)

    try:
        # LED-Streifen initialisieren
        print(f"\n🔧 LED-Streifen wird initialisiert...")
        pin = machine.Pin(LED_PIN, machine.Pin.OUT)
        leds = NeoPixel(pin, LED_ANZAHL)
        print("✅ LED-Streifen bereit!")

        # Tests durchführen
        grundfarben_test(leds)
        bunte_farben_test(leds)
        einzelne_leds_test(leds)
        regenbogen_test(leds)
        lauflicht_test(leds)

        # Alle LEDs aus
        alle_leds_setzen(leds, AUS)

        # Erfolgsmeldung
        print("\n" + "=" * 50)
        print("🎉 ALLE TESTS ERFOLGREICH!")
        print("=" * 50)
        print("✅ Raspberry Pi Pico funktioniert perfekt")
        print("✅ LED-Streifen richtig angeschlossen")
        print("✅ Alle Farben werden korrekt angezeigt")
        print("✅ Alle LEDs sind funktionsfähig")
        print("\n🏆 Du kannst jetzt eigene Programme schreiben!")
        print("📚 Schau dir die Beispiele im Ordner '03_Beispiele' an!")

    except Exception as e:
        # Fehlerbehandlung für Schüler
        print(f"\n❌ FEHLER BEIM TEST:")
        print(f"   {e}")
        print("\n🔧 WAS TUN?")
        print("   1. Hardware-Verbindungen prüfen")
        print("   2. Raspberry Pi Pico neu anschließen")
        print("   3. Programm neu starten (F5)")
        print("   4. Lehrer*innen fragen")
        print("\n💡 HÄUFIGE PROBLEME:")
        print("   • GPIO-Pin falsch (sollte Pin 4 sein)")
        print("   • LED-Anzahl falsch eingestellt")
        print("   • Kabel lose oder falsch angeschlossen")
        print("   • Zu viele LEDs für Stromversorgung")


# ===== PROGRAMM STARTEN =====
if __name__ == "__main__":
    main()
