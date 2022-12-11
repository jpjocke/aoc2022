class Operation:
    op: str

    def calc_new_level(self, item: int):
        split = self.op.split(" ")
        if split[2] == "old":
            second = item
        else:
            second = int(split[2])
        if split[1] == "+":
            return item + second
        elif split[1] == "*":
            return item * second
        raise BaseException(f"unknown op: {self.op}")
