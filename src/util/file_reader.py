from typing import List


class FileReader:

    def read(self, path: str) -> str:
        with open(path, 'r') as f:
            data = f.read()
        return data

    def read_as_str_lines(self, path: str) -> List[str]:
        return self.read(path).splitlines()

    def read_as_int_lines(self, path: str) -> List[int]:
        return [*map(int, self.read_as_str_lines(path))]
