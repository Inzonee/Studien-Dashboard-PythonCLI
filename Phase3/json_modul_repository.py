import json
from pathlib import Path
from datetime import date

from modul import Modul
from modul_repository import ModulRepository
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung

class JsonModulRepository(ModulRepository):
    def __init__(self, dateipfad: str):
        self.dateipfad = Path(dateipfad)

    def lade_alle(self) -> list[Modul]:
        if not self.dateipfad.exists():
            return []
        with self.dateipfad.open("r", encoding="utf-8") as datei:
            daten = json.load(datei)

        module: list[Modul] = []
        for modul_daten in daten:
            pruefungsleistungen = []
            for p_daten in modul_daten["pruefungsleistungen"]:
                pruefungsleistungen.append(Pruefungsleistung(note=p_daten["note"]))

            modul = Modul(
                name=modul_daten["name"],
                ects=modul_daten["ects"],
                status=ModulStatus(modul_daten["status"]),
                semester_nummer=modul_daten["semester_nummer"],
                pruefungsleistungen=pruefungsleistungen,
                startdatum=date.fromisoformat(modul_daten["startdatum"]) if modul_daten["startdatum"] else None,
                abschlussdatum=date.fromisoformat(modul_daten["abschlussdatum"]) if modul_daten["abschlussdatum"] else None,
            )
            module.append(modul)

        return module

    def speichere(self, modul: Modul) -> None:
        module = self.lade_alle()
        module.append(modul)
        
        daten = [self._modul_als_dict(m) for m in module]

        with self.dateipfad.open("w", encoding="utf-8") as datei:
            json.dump(daten, datei, ensure_ascii=False, indent=4)

    def _modul_als_dict(self, modul: Modul) -> dict:
        return {
            "name": modul.name,
            "ects": modul.ects,
            "status": modul.status.value,
            "semester_nummer": modul.semester_nummer,
            "pruefungsleistungen": [{"note": p.note} for p in modul.pruefungsleistungen],
            "startdatum": modul.startdatum.isoformat() if modul.startdatum else None,
            "abschlussdatum": modul.abschlussdatum.isoformat() if modul.abschlussdatum else None,
        }

