from studiengang import Studiengang 
from modul_status import ModulStatus
from datetime import date

class StudienService:
    def berechne_notendurchschnitt(self,studiengang: Studiengang) -> float | None:
        alle_noten = []
        for semester in studiengang.semester:
            for modul in semester.module:
                for pruefung in modul.pruefungsleistungen:
                    if pruefung.note is not None:
                        alle_noten.append(pruefung.note)
        if len(alle_noten) == 0 :
            return None
        return sum(alle_noten) / len(alle_noten)

    def berechne_tempo(self, studiengang: Studiengang) -> tuple[float|None,float| None]:
        bisher_erreichte_ects = 0
        for semester in studiengang.semester:
            for module in semester.module:
                if module.status == ModulStatus.ABGESCHLOSSEN:
                    bisher_erreichte_ects += module.ects
        heute = date.today()

        # monate seit studienstart berrechnung
        vergangene_tage = (heute -studiengang.startdatum).days
        vergangene_monate = vergangene_tage / 30

        if vergangene_monate <= 0:
            bisheriges_tempo= None
        else:
            bisheriges_tempo = bisher_erreichte_ects / vergangene_monate


        # monate bis Zielabschluss
        verbleibende_tage = (studiengang.ziel_abschlussdatum - heute).days
        verbleibende_monate = verbleibende_tage / 30
        if vergangene_monate <= 0:
            bisheriges_tempo= None
        else:
            restliche_ects = studiengang.gesamt_ects - bisher_erreichte_ects
            benoetigtes_tempo = restliche_ects / verbleibende_monate
        return bisheriges_tempo, benoetigtes_tempo


    






