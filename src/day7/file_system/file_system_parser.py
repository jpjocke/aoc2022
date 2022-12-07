from typing import List

from src.day7.file_system.directory import Directory
from src.day7.file_system.file import File


class FileSystemParser:
    root: Directory
    current_loc: Directory
    current_row: int
    data: List[str]

    def parse_file_system(self, data: List[str]) -> Directory:
        self.root = Directory(parent=None, name="root")
        self.current_loc = self.root
        self.current_row = 0
        self.data = data

        while self.current_row < len(self.data):
            self._parse_row()
            self.current_row += 1
        return self.root

    def _parse_row(self):
        split = self.data[self.current_row].split(" ")
        if split[0] == "$":
            self._parse_command(split)
        self.current_row

    def _parse_command(self, split: List[str]):
        print("command")
        if split[1] == "cd":
            if split[2] == "/":
                self.current_loc = self.root
            elif split[2] == "..":
                self.current_loc = self.current_loc.parent
            else:
                self.current_loc = self.current_loc.get_dir_from_name(name=split[2])
        if split[1] == "ls":
            print("iterate over listed files")
            self._parse_ls()

    def _parse_ls(self):
        while True:
            self.current_row += 1
            split = self.data[self.current_row].split(" ")
            if split[0] == "dir":
                print("directory")
                directory = Directory(parent=self.current_loc, name=split[1])
                self.current_loc.add_dir(directory)
            else:
                print("file")
                file = File(name=split[1], size=int(split[0]))
                self.current_loc.add_file(file)
            if self._is_next_line_command():
                return

    def _is_next_line_command(self) -> bool:
        if self.current_row + 1 == len(self.data):
            return True
        split = self.data[self.current_row + 1].split(" ")
        if split[0] == "$":
            return True
        return False
