from enum import Enum

class ModulStatus(str, Enum):
    OFFEN = "offen"
    IN_BEARBEITUNG = "in_bearbeitung"
    ABGESCHLOSSEN = "abgeschlossen"

