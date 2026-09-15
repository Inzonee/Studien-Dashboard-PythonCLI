from modul_repository import ModulRepository
from studien_service import StudienService
from studiengang import Studiengang
from semester import Semester
from abschlussgrad import Abschlussgrad
from datetime import date

class DashboardController:
    """Vermittelt zwischen Repository/Service und
    der CLI. Baut aus den flach gespeicherten Modulen wieder eine
    vollstaendige Studiengang-Struktur mit Semestern zusammen"""
    def __init__(self, modul_repository: ModulRepository,studien_service: StudienService):
        self.modul_repository = modul_repository
        self.studien_service = studien_service

    def lade_dashboard_daten(self) -> dict:
        module = self.modul_repository.lade_alle()

        semester_dict: dict[int, list] = {}
        for modul in module:
            semester_dict.setdefault(modul.semester_nummer, []).append(modul)

        semester_liste = []
        for nummer in sorted(semester_dict.keys()):
            semester_liste.append(Semester(nummer=nummer, module=semester_dict[nummer]))

        studiengang = Studiengang(
            name="IT-Security",
            abschlussgrad=Abschlussgrad.BACHELOR,
            gesamt_ects=180,
            startdatum=date(2026, 1, 1),
            ziel_abschlussdatum=date(2028, 8, 1),
            ziel_notendurchschnitt=2.0,
            semester=semester_liste,
        )

        notendurchschnitt = self.studien_service.berechne_notendurchschnitt(studiengang)
        bisheriges_tempo, benoetigtes_tempo = self.studien_service.berechne_tempo(studiengang)

        return {
            "studiengang": studiengang,
            "notendurchschnitt": notendurchschnitt,
            "bisheriges_tempo": bisheriges_tempo,
            "benoetigtes_tempo": benoetigtes_tempo,
            "fortschritt_prozent": self.studien_service.berechne_fortschritt_prozent(studiengang),
            "voraussichtliches_abschlussdatum": self.studien_service.berechne_voraussichtliches_abschlussdatum(studiengang),
        }