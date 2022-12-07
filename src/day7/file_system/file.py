class File:
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} {self.size}"
