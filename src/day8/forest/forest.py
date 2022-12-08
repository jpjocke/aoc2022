from typing import List


class Forest:
    forest: List[List[int]]
    visible: List[List[int]]

    def __init__(self, data: List[str]):
        self.forest = []
        self.visible = []
        for row in data:
            fr = []
            self.forest.append(fr)
            vr = []
            self.visible.append(vr)
            for letter in row:
                fr.append(int(letter))
                vr.append(0)

    def find_visible(self) -> int:
        self._compare_l_to_r()
        self._compare_r_to_l()
        self._compare_u_to_d()
        self._compare_d_to_u()
        count = 0
        for row in self.visible:
            for visible in row:
                count += visible
        return count

    def _compare_l_to_r(self):
        i = 0
        j = 0
        highest = -1
        while True:
            highest = self._compare_highest(highest, i, j)
            j += 1
            if j >= len(self.forest[i]) or highest == 9:
                i += 1
                j = 0
                highest = -1
            if i >= len(self.forest):
                break

    def _compare_r_to_l(self):
        i = 0
        j = len(self.forest[i]) - 1
        highest = -1
        while True:
            highest = self._compare_highest(highest, i, j)
            j -= 1
            if j < 0 or highest == 9:
                i += 1
                j = len(self.forest[0]) - 1
                highest = -1
            if i >= len(self.forest):
                break

    def _compare_u_to_d(self):
        i = 0
        j = 0
        highest = -1
        while True:
            highest = self._compare_highest(highest, i, j)
            i += 1
            if i >= len(self.forest) or highest == 9:
                i = 0
                j += 1
                highest = -1
            if j >= len(self.forest[0]):
                break

    def _compare_d_to_u(self):
        i = len(self.forest) - 1
        j = 0
        highest = -1
        while True:
            highest = self._compare_highest(highest, i, j)
            i -= 1
            if i < 0 or highest == 9:
                i = len(self.forest) - 1
                j += 1
                highest = -1
            if j >= len(self.forest[0]):
                break

    def _compare_highest(self, highest, i, j):
        if self.forest[i][j] > highest:
            self.visible[i][j] = 1
            highest = self.forest[i][j]
        return highest
