
from modul_status import ModulStatus
class DashboardCLI:
    def anzeigen(self,daten: dict) -> None:
        studiengang = daten["studiengang"]
        print(f"Studiengang: {studiengang.name} ({studiengang.abschlussgrad.value})")
        print(f"Ziel-Notendurchschnitt: {studiengang.ziel_notendurchschnitt}")
        print()

        nd = daten["notendurchschnitt"]
        print(f"Aktueller Notendurchschnitt: {round(nd, 2) if nd is not None else 'noch keine Note vorhanden'}")

        ziel = studiengang.ziel_notendurchschnitt
        if nd is not None:
            abweichung = nd - ziel
            if abweichung <= 0:
                print(f"Notenziel: erreicht ({round(nd, 2)} bei Ziel {ziel})")
            else:
                    print(f"Notenziel: nicht erreicht (+{round(abweichung, 2)})")
        else:
            print("Notenziel: noch nicht bewertbar (keine Note vorhanden)")






        bt = daten["bisheriges_tempo"]
        print(f"Bisheriges Tempo: {round(bt, 2) if bt is not None else 'noch nicht berechenbar'} ECTS/Monat")

        bn = daten["benoetigtes_tempo"]
        print(f"Benoetigtes Tempo: {round(bn, 2) if bn is not None else 'noch nicht berechenbar'} ECTS/Monat")
        fp = daten["fortschritt_prozent"]
        print(f"Fortschritt: {round(fp, 1)}%")

        vad = daten["voraussichtliches_abschlussdatum"]
        print(f"Voraussichtlicher Abschluss: {vad.strftime('%B %Y') if vad else 'noch nicht berechenbar'}")

        if vad is not None:
            ziel_datum = studiengang.ziel_abschlussdatum
            if vad <= ziel_datum:
                 print(f"Zeitziel: erreichbar (Ziel: {ziel_datum.strftime('%B %Y')})")
            else:
                verzug_monate = (vad.year - ziel_datum.year) * 12 + (vad.month - ziel_datum.month)
                print(f"Zeitziel: nicht erreichbar bei aktuellem Tempo (ca. {verzug_monate} Monate Spät)")
        else:
            print("Zeitziel: noch nicht bewertbar (Tempo noch nicht berechenbar)")
                





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