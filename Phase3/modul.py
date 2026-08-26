from dataclasses import dataclass, field
from datetime import date
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung

@dataclass

class Modul:
    name: str
    ects: int
    status: ModulStatus
    pruefungsleistung: list[Pruefungsleistung] = field(default_factory=list)
    startdatum: date | None = None
    abschlussdatum: date | None = None

    @property
    def bearbeitungsdauer_tage(self) -> int |None:
        if self.startdatum is None or self.abschlussdatum is None:
            return None
        return (self.abschlussdatum - self.startdatum).days
    

