from typing import List

from src.day13.packets.packet import Packet


def check_packets(packets: List[Packet]):
    count = 0
    for i, p in enumerate(packets):
        # p.print()
        if p.is_in_correct_order():
            count += i + 1
    return count
