from enum import Enum

class ModulStatus(str, Enum):
    """Bildet den Bearbeitungsstatus eines Moduls ab."""
    OFFEN = "offen"
    IN_BEARBEITUNG = "in_bearbeitung"
    ABGESCHLOSSEN = "abgeschlossen"

