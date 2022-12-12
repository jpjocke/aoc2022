from src.util.point import Point


class HeightMapPoint:
    p: Point
    value: int
    height: str
    start_point: bool
    end_point: bool

    def __init__(self):
        self.start_point = False
        self.end_point = False

    def __str__(self):
        return f"{self.p.__str__()}: {self.height}, {self.value}"