
from modul_status import ModulStatus
class DashboardCLI:
    def anzeigen(self,daten: dict) -> None:
        studiengang = daten["studiengang"]
        print(f"Studiengang: {studiengang.name} ({studiengang.abschlussgrad.value})")
        print(f"Ziel-Notendurchschnitt: {studiengang.ziel_notendurchschnitt}")
        print()

        nd = daten["notendurchschnitt"]
        print(f"Aktueller Notendurchschnitt: {round(nd, 2) if nd is not None else 'noch keine Note vorhanden'}")

        bt = daten["bisheriges_tempo"]
        print(f"Bisheriges Tempo: {round(bt, 2) if bt is not None else 'noch nicht berechenbar'} ECTS/Monat")

        bn = daten["benoetigtes_tempo"]
        print(f"Benoetigtes Tempo: {round(bn, 2) if bn is not None else 'noch nicht berechenbar'} ECTS/Monat")
        fp = daten["fortschritt_prozent"]
        print(f"Fortschritt: {round(fp, 1)}%")

        vad = daten["voraussichtliches_abschlussdatum"]
        print(f"Voraussichtlicher Abschluss: {vad.strftime('%B %Y') if vad else 'noch nicht berechenbar'}")

        print()
        print("Bearbeitete Module:")
        for semester in studiengang.semester:
            for modul in semester.module:
                if modul.status == ModulStatus.ABGESCHLOSSEN:
                    print(f"  - {modul.name} ({modul.ects} ECTS)")

        print()
        print("Offene Module:")
        for semester in studiengang.semester:
            for modul in semester.module:
                if modul.status != ModulStatus.ABGESCHLOSSEN:
                    print(f" - {modul.name} ({modul.ects} ECTS, {modul.status.value})")