class Instruction:
    amount: int
    fr: int
    to: int

    def __init__(self, amount: int, fr: int, to: int):
        self.amount = amount
        self.fr = fr
        self.to = to

    def __str__(self):
        return f"{self.amount}, {self.fr}, {self.to}"