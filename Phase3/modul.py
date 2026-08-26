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
    
    

