from dataclasses import dataclass
from model.state import State

@dataclass
class Border:
    s1Id: int
    s2Id: int
    year: int
