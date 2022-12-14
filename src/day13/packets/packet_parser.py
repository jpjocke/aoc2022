import json
from typing import List

from src.day13.packets.packet import Packet


def parse_packets(data: List[str]) -> List[Packet]:
    packets = []
    p = Packet()
    packets.append(p)
    for row in data:
        # print(row)
        if len(row) == 0:
            continue
        if p.left is not None and p.right is not None:
            p = Packet()
            packets.append(p)
        tt = "{\"a\":" + row + "}"
        # print(tt)
        j = json.loads("{\"a\":" + row + "}")
        if p.left is None:
            p.left = j["a"]
        else:
            p.right = j["a"]
        # print(type(j["a"]))
        # if type(j["a"]) == list:
        #     print("its a list")
    return packets
