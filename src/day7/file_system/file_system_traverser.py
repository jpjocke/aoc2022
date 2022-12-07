from typing import List

from src.day7.file_system.directory import Directory


def find_total_size_for_problem_1(root: Directory) -> int:
    dirs = find_all_dirs_with_max_size(root=root, max_size=100000)
    total_size = 0
    for d in dirs:
        total_size += d.size()
    return total_size


def find_size_delete_for_problem_2(root: Directory) -> int:
    disc_size = 70000000
    need = 30000000
    current_size = root.size()
    min_size_delete = current_size - (disc_size - need)
    dirs = find_all_dirs_with_min_size(root=root, min_size=min_size_delete)
    sizes = [d.size() for d in dirs]
    sizes.sort()
    return sizes[0]


def find_all_dirs_with_max_size(root: Directory, max_size: int) -> List[Directory]:
    dirs = []
    _find_dirs_recursive_max_size(dirs, max_size, root)
    return dirs


def _find_dirs_recursive_max_size(dirs: List[Directory], max_size: int, root_dir: Directory):
    for d in root_dir.dirs:
        if d.size() < max_size:
            dirs.append(d)
        _find_dirs_recursive_max_size(dirs=dirs, max_size=max_size, root_dir=d)


def find_all_dirs_with_min_size(root: Directory, min_size: int) -> List[Directory]:
    dirs = []
    if root.size() > min_size:
        dirs.append(root)
    _find_dirs_recursive_min_size(dirs, min_size, root)
    return dirs


def _find_dirs_recursive_min_size(dirs: List[Directory], min_size: int, root_dir: Directory):
    for d in root_dir.dirs:
        if d.size() > min_size:
            dirs.append(d)
        _find_dirs_recursive_min_size(dirs=dirs, min_size=min_size, root_dir=d)
