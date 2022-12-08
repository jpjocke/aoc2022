from typing import List


class Forest:
    forest: List[List[int]]
    visible: List[List[int]]
    scenic: List[List[int]]

    def __init__(self, data: List[str]):
        self.forest = []
        self.visible = []
        self.scenic = []
        for row in data:
            fr = []
            self.forest.append(fr)
            vr = []
            self.visible.append(vr)
            scenic = []
            self.scenic.append(scenic)
            for letter in row:
                fr.append(int(letter))
                vr.append(0)
                scenic.append(0)

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

    def find_scenic(self) -> int:
        # dont check edges
        i = 1
        j = 1
        while True:
            up = self._scenic_score(i, j, 0)
            down = self._scenic_score(i, j, 1)
            left = self._scenic_score(i, j, 2)
            right = self._scenic_score(i, j, 3)
            self.scenic[i][j] = up * down * left * right
            j += 1
            if j >= len(self.forest[i]) - 1:
                i += 1
                j = 0
            if i >= len(self.forest) - 1:
                break

        top_score = 0

        for row in self.scenic:
            for score in row:
                if score > top_score:
                    top_score = score
        return top_score

    def _scenic_score(self, i: int, j: int, dir: int) -> int:
        # 0 down
        # 1 up
        # 2 left
        # 3 right0
        height = self.forest[i][j]
        score = 0
        while True:
            if dir == 0:
                i -= 1
            elif dir == 1:
                i += 1
            elif dir == 2:
                j -= 1
            else:
                j += 1
            if i < 0 or j < 0 or i >= len(self.forest) or j >= len(self.forest[0]):
                return score
            if self.forest[i][j] >= height:
                return score + 1
            score += 1
