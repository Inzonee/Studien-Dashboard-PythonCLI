from dataclasses import dataclass, field
from datetime import date
from modul import Modul
from modul_status import ModulStatus


@dataclass

class Semester:
    nummer: int
    module: list[Modul] = field(default_factory=list)

    @property
    def startdatum(self) -> date | None:
        gestartete_module = []
        for m in self.module:
            if m.startdatum is not None:
                gestartete_module.append(m.startdatum)
        if len(gestartete_module) == 0:
            return None
        return min(gestartete_module)

    @property
    def enddatum(self) -> date | None:
        abgeschlossene_module = []
        for m in self.module:
            if m.status == ModulStatus.ABGESCHLOSSEN and m.abschlussdatum is not None:
                abgeschlossene_module.append(m.abschlussdatum)

        if len(abgeschlossene_module) == 0:
            return None
        return max(abgeschlossene_module)
