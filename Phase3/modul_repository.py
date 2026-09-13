from modul import Modul
from abc import ABC, abstractmethod

class ModulRepository(ABC):
    """Definiert welche Methoden ein Repository anbietenMuss.
    Legt nicht fest, wie gespeichert wird."""

    @abstractmethod
    def lade_alle(self) -> list[Modul]:
        pass
    @abstractmethod
    def speichere(self,modul: Modul) -> None:
        pass