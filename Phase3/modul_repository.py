from modul import Modul
from abc import ABC, abstractmethod

class ModulRepository(ABC):

    @abstractmethod
    def lade_alle(self) -> list[Modul]:
        pass
    @abstractmethod
    def speichere(self,modul: Modul) -> None:
        pass