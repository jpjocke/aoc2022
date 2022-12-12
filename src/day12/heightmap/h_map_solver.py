from typing import Dict, List

from src.day12.heightmap.h_map import HeightMap
from src.day12.heightmap.h_map_point import HeightMapPoint
from src.util.util import point_to_key


class HeightMapSolver:
    h_map: HeightMap
    visited_map = Dict[str, int]
    to_visit_list = List[HeightMapPoint]
    end_found: bool

    def __init__(self, h_map: HeightMap):
        self.h_map = h_map
        self.to_visit_list = [h_map.start]
        self.visited_map = {point_to_key(h_map.start.p): 0}
        self.end_found = False

    def solve_shortest(self) -> int:
        while len(self.to_visit_list) > 0:
            # next_h_map = self.to_visit_list.pop(0)
            next_h_map = self._get_next()
            print(f"solving for {next_h_map}")
            self._update_closest(next_h_map)
            if self.end_found:
                break

        end_key = point_to_key(self.h_map.end.p)
        return self.visited_map[end_key]

    def _get_next(self) -> HeightMapPoint:
        lowest = 99999999
        for p in self.to_visit_list:
            if self.visited_map[point_to_key(p.p)] < lowest:
                ret = p
                lowest = self.visited_map[point_to_key(p.p)]
        self.to_visit_list.remove(ret)
        return ret

    def _update_closest(self, h_map_point: HeightMapPoint):
        p_now = h_map_point.p
        current_move = self.visited_map[point_to_key(p_now)]
        if p_now.x > 0:
            self._compare(h_map_point, self.h_map.map[p_now.y][p_now.x - 1], current_move)
        if p_now.x < len(self.h_map.map[0]) - 1:
            self._compare(h_map_point, self.h_map.map[p_now.y][p_now.x + 1], current_move)
        if p_now.y > 0:
            self._compare(h_map_point, self.h_map.map[p_now.y - 1][p_now.x], current_move)
        if p_now.y < len(self.h_map.map) - 1:
            self._compare(h_map_point, self.h_map.map[p_now.y + 1][p_now.x], current_move)

    def _compare(self, h_now: HeightMapPoint, h_next: HeightMapPoint, current_move: int):
        if h_now.value + 1 < h_next.value:
            return
        key_next = point_to_key(h_next.p)
        move_next = current_move + 1
        if key_next in self.visited_map:
            if self.visited_map[key_next] > move_next:
                self.visited_map[key_next] = move_next
                self.to_visit_list.append(h_next)
        else:
            self.visited_map[key_next] = move_next
            self.to_visit_list.append(h_next)
        if h_next.end_point:
            self.end_found = True
