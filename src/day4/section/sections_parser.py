from typing import Tuple, List

from src.day4.section.Sections import Sections


def parse_sections(rows: List[str]) -> List[Tuple[Sections, Sections]]:
    sections_list = []
    for row in rows:
        a, b = row.split(",")
        sections_list.append((_parse_sections_single(a), _parse_sections_single(b)))
    return sections_list


def _parse_sections_single(raw: str) -> Sections:
    start, end = raw.split("-")
    return Sections(int(start), int(end))


def count_fits(sections_list=List[Tuple[Sections, Sections]]) -> int:
    count = 0
    for a, b in sections_list:
        if a.fits_in_other(b):
            count += 1
    return count


def count_overlaps(sections_list=List[Tuple[Sections, Sections]]) -> int:
    count = 0
    for a, b in sections_list:
        if a.overlap(b):
            count += 1
    return count
