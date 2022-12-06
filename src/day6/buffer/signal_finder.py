def find_start_of_packet(signal: str) -> int:
    return _find_distinct_chars(signal, 0, 4)


def find_start_of_message(signal: str, start: int) -> int:
    return _find_distinct_chars(signal=signal, start=start, amount=14)


def _find_distinct_chars(signal: str, start: int, amount: int) -> int:
    ending = start + amount
    while True:
        if _list_has_distinct_chars(signal[start:ending]):
            return ending
        start += 1
        ending += 1
    return 0


def _list_has_distinct_chars(small_signal: str) -> bool:
    for i, let_a in enumerate(small_signal):
        if i == len(small_signal) - 1:
            break
        if let_a in small_signal[i + 1:]:
            return False

    return True
