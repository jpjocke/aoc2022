from util.file_reader import FileReader

fr = FileReader()
data = fr.read_as_int_lines("../../data/dayX_in.txt")

for d in data:
    print(d)
