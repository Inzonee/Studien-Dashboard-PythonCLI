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
    def berechne_fortschritt_prozent(self, studiengang: Studiengang) -> float:
        bisher_erreichte_ects = 0
        for semester in studiengang.semester:
            for modul in semester.module:
                if modul.status == ModulStatus.ABGESCHLOSSEN:
                    bisher_erreichte_ects += modul.ects

        if studiengang.gesamt_ects == 0:
            return 0.0
        return bisher_erreichte_ects / studiengang.gesamt_ects * 100
    
    def berechne_voraussichtliches_abschlussdatum(self, studiengang: Studiengang) -> date | None:
        bisheriges_tempo, _ = self.berechne_tempo(studiengang)

        if bisheriges_tempo is None or bisheriges_tempo == 0:
            return None

        bisher_erreichte_ects = 0
        for semester in studiengang.semester:
            for modul in semester.module:
                if modul.status == ModulStatus.ABGESCHLOSSEN:
                    bisher_erreichte_ects += modul.ects

        restliche_ects = studiengang.gesamt_ects - bisher_erreichte_ects
        benoetigte_monate = restliche_ects / bisheriges_tempo

        heute = date.today()
        gesamt_monate = heute.month - 1 + benoetigte_monate
        jahre_dazu = int(gesamt_monate // 12)
        neuer_monat = int(gesamt_monate % 12) + 1

        return date(heute.year + jahre_dazu, neuer_monat, 1)






