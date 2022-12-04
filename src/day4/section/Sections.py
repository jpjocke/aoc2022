class Sections:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def size(self) -> int:
        return self.end - self.start

    def fits_in_other(self, other: "Sections") -> bool:
        if self.start >= other.start and self.end <= other.end:
            return True
        if other.start >= self.start and other.end <= self.end:
            return True
        return False

    def overlap(self, other: "Sections") -> bool:
        if other.start <= self.start <= other.end:
            return True
        if other.start <= self.end <= other.end:
            return True
        if self.start <= other.start <= self.end:
            return True
        if self.start <= other.end <= self.end:
            return True
        return False