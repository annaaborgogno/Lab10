from dataclasses import dataclass

@dataclass
class State:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.StateAbb)

    def __eq__(self, other):
        return self.CCode == other.CCode

    def __str__(self):
        return f"{self.StateNme} - ({self.StateAbb})"

    def __lt__(self, other):
        return self.StateNme < other.StateNme