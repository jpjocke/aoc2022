from typing import List

from src.day7.file_system.file import File


class Directory:
    parent: "Directory"
    name: str
    dirs: List["Directory"]
    files: List[File]

    def __init__(self, parent: "Directory", name: str):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def add_dir(self, directory: "Directory"):
        self.dirs.append(directory)

    def add_file(self, file: File):
        self.files.append(file)

    def size(self) -> int:
        size = 0
        for d in self.dirs:
            size += d.size()
        for f in self.files:
            size += f.size
        return size

    def get_dir_from_name(self, name: str) -> "Directory":
        for d in self.dirs:
            if d.name == name:
                return d
        raise BaseException(f"No dir with name: {name}")

    def print(self, indent: int = 0):
        print(f"{indent * '  '}- {self.name} (dir)")
        for d in self.dirs:
            d.print(indent=indent + 1)
        for f in self.files:
            print(f"{(indent + 1) * '  '}- {f}")

    def __str__(self):
        return f"{self.name}, dirs: ({[d.__str__() for d in self.dirs]}), files: ({[f.__str__() for f in self.files]})"
