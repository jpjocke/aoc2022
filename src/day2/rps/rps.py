ROCK = "rock"
PAPER = "paper"
SCISSOR = "scissor"


class RPS:
    type: str

    def __init__(self, type: str):
        self.type = type

    def score(self, other: "RPS") -> int:
        # (1 for Rock, 2 for Paper, and 3 for Scissors)
        # (0 if you lost, 3 if the round was a draw, and 6 if you won)
        score = 0
        if self.type == ROCK:  # +1
            if other.type == PAPER:
                return 1
            if other.type == SCISSOR:
                return 7
            return 4
        if self.type == PAPER:
            if other.type == PAPER:
                return 5
            if other.type == SCISSOR:
                return 2
            return 8
        # SCISSOR
        if other.type == PAPER:
            return 9
        if other.type == SCISSOR:
            return 6
        return 3
