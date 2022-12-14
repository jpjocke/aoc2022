from typing import List, Any

from src.day13.packets.packet import Packet


def check_packets(packets: List[Packet]) -> int:
    count = 0
    for i, p in enumerate(packets):
        # p.print()
        if p.is_in_correct_order():
            count += i + 1
    return count


def sort_two(packets: List[List[Any]]) -> int:
    packet_one = [[2]]
    packet_two = [[6]]
    packet_one_place = 1
    packet_two_place = 2
    for p_l in packets:
        p = Packet()
        p.left = p_l
        p.right = packet_one

        if p.is_in_correct_order():
            packet_one_place += 1
            packet_two_place += 1
        else:
            p = Packet()
            p.left = p_l
            p.right = packet_two
            if p.is_in_correct_order():
                packet_two_place += 1

    return packet_one_place * packet_two_place
