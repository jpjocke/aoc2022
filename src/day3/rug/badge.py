from typing import List


class Badge:
    items: List[str]

    def __init__(self):
        self.items = []

    def add(self, item: str):
        self.items.append(item)

    def find_badge(self) -> str:
        for a in self.items[0]:
            if a in self.items[1]:
                if a in self.items[2]:
                    return a
