from enum import Enum
from dataclasses import dataclass, field
from datetime import date
from abschlussgrad import Abschlussgrad
from semester import Semester


@dataclass
class Studiengang:
    """repräsentiert den gesamten Studiengang mit seinen Zielwerten uind der Liste der zugehörigen Semester"""
    name : str
    abschlussgrad : Abschlussgrad 
    gesamt_ects: int
    
    startdatum : date
    ziel_abschlussdatum : date
    ziel_notendurchschnitt : float
    semester : list[Semester] = field(default_factory=list)



if __name__ == "__main__":
    mein_studiengang = Studiengang(
        name="test",
        abschlussgrad= Abschlussgrad.BACHELOR ,
        gesamt_ects=180,
        startdatum=date(2000, 1, 1),
        ziel_abschlussdatum=date(2045, 1, 1),
        ziel_notendurchschnitt= 0.1
    )
    print(mein_studiengang)