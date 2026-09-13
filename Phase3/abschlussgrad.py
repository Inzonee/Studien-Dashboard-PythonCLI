from enum import Enum

class Abschlussgrad(str,Enum):
    """Bildet den Abschlussgrad ab."""
    BACHELOR = "bachelor"
    MASTER = "master"