class RugSack:
    first: str
    second: str

    def __init__(self, whole: str):
        half = int(len(whole) / 2)
        self.first = whole[:half]
        self.second = whole[half:]

    def find_duplicates(self) -> str:
        sb = ''
        found = set()
        for a in self.first:
            for b in self.second:
                if a == b:
                    #sb += a
                    found.add(a)
        for key in found:
            sb += key
        return sb
