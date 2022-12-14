class CavernPoint:
    rock: bool
    air: bool
    sand: bool

    def __init__(self):
        self.rock = False
        self.air = True
        self.sand = False

    def is_occupied(self) -> bool:
        if self.rock:
            return True
        if self.sand:
            return True
        return False

    def __str__(self):
        if self.rock:
            return "#"
        if self.sand:
            return "o"
        return "."
