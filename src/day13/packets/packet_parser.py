import json
from typing import List

from src.day13.packets.packet import Packet


def parse_packets(data: List[str]) -> List[Packet]:
    packets = []
    p = Packet()
    packets.append(p)
    for row in data:
        if len(row) == 0:
            continue
        if p.left is not None and p.right is not None:
            p = Packet()
            packets.append(p)
        j = json.loads("{\"a\":" + row + "}")
        if p.left is None:
            p.left = j["a"]
        else:
            p.right = j["a"]
    return packets


def parse_packets_2(data: List[str]) -> List[Packet]:
    packets = []
    for row in data:
        if len(row) == 0:
            continue
        j = json.loads("{\"a\":" + row + "}")
        packets.append(j["a"])
    return packets
