# Studien Dashboard

Prototypische Umsetzung eines Studien-Dashboards (Projekt: Objektorientierte und funktionale Programmierung mit Python).

## Voraussetzungen
- Python 3.10 oder neuer
- Keine externen Pakete nötig (nur Standardbibliothek)

## Installation
1. Repository klonen:
   `git clone https://github.com/Inzonee/Studien-Dashboard-PythonCLI.git`
2. In den Ordner wechseln:
   cd Studien-Dashboard-PythonCLI/Phase3
3. Programm starten:
   python studium_dashboard_app.py

## Testdaten
Im Ordner Phase3 liegt bereits eine `module.json` mit Beispieldaten. Um später eigene Module hinzuzufügen benutze folgendes template und kopiere die in module.json datei hinein:

```json
{
    "name": "Name des Moduls",
    "ects": 5,
    "status": "offen",
    "semester_nummer": 1,
    "pruefungsleistungen": [{"note": null}],
    "startdatum": null,
    "abschlussdatum": null
}
```

**WICHTIG!!**
- `status`: muss exakt einer von drei Werten sein: `"offen"`,
  `"in_bearbeitung"`, `"abgeschlossen"` (Kleinschreibung beachten,
  sonst Fehler beim Programmstart)
- `startdatum`/`abschlussdatum`: Format `"JJJJ-MM-TT"` (z.B.
  `"2026-08-07"`), oder `null` (ohne Anfuehrungszeichen), falls noch
  nicht bekannt
    - **Beispiel**:
    - `2026-08-07` RICHTIG
    - `2026-08-7`  **FALSCH**
- `pruefungsleistungen`: Liste von Objekten mit `"note"`. `null`
  bedeutet noch nicht bewertet, sonst eine Zahl wie `2.0`