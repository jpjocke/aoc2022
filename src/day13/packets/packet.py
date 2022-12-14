from typing import List, Any


class Packet:
    left: List[Any]
    right: List[Any]
    is_in_right_order_v: bool

    def __init__(self):
        self.left = None
        self.right = None
        self.is_in_right_order_v = None

    def is_in_correct_order(self) -> bool:
        self._is_in_correct_order(self.left, self.right)
        return self.is_in_right_order_v

    def _is_in_correct_order(self, l: Any, r: Any):
        # print(f"compare {l} vs {r}")
        if self.is_in_right_order_v is not None:
            return
        if type(l) == int and type(r) == int:
            # print("both ints")
            if l > r:
                self.is_in_right_order_v = False
                return
            if l < r:
                self.is_in_right_order_v = True
                return
        elif type(l) == list and type(r) == list:
            # print("both lists")
            i = 0
            while True:
                if len(l) - 1 < i <= len(r) - 1:
                    # left is shorter than right
                    self.is_in_right_order_v = True
                    return
                if len(r) - 1 < i <= len(l) - 1:
                    # right is shorter than left
                    self.is_in_right_order_v = False
                    return

                if len(l) == len(r):
                    if i >= len(l):
                        break
                self._is_in_correct_order(l[i], r[i])
                if self.is_in_right_order_v is not None:
                    return
                i += 1
        else:
            if type(l) == int:
                # print("left int")
                self._is_in_correct_order([l], r)
            else:
                # print("right int")
                self._is_in_correct_order(l, [r])

    def print(self):
        print("===================================")
        print("LEFT")
        print(self.left)
        for item in self.left:
            self._print_item(item)
        print("RIGHT")
        print(self.right)
        for item in self.right:
            self._print_item(item)

    def _print_item(self, item: List[Any]):
        print(item)
        if type(item) == list:
            for inner_item in item:
                self._print_item(inner_item)
