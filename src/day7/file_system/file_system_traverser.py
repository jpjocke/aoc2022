from typing import List

from src.day7.file_system.directory import Directory


def find_total_size_for_problem_1(root: Directory) -> int:
    dirs = find_all_dirs_with_size(root=root, max_size=100000)
    total_size = 0
    for d in dirs:
        total_size += d.size()
    return total_size


def find_all_dirs_with_size(root: Directory, max_size: int) -> List[Directory]:
    dirs = []
    _find_dirs_recursive(dirs, max_size, root)
    return dirs


def _find_dirs_recursive(dirs: List[Directory], max_size: int, root_dir: Directory):
    for d in root_dir.dirs:
        if d.size() < max_size:
            dirs.append(d)
        _find_dirs_recursive(dirs=dirs, max_size=max_size, root_dir=d)
