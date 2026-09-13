from dataclasses import dataclass

@dataclass

class Pruefungsleistung:
    """Repräsentiert die einzele Note eines Moduls. Note ist optimal, da eine Pruefungsleistung existieren kann, bevor sie bewertet wurde. """
    note: float | None  = None 
    