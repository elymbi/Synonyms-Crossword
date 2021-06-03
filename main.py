from crossword3 import *


def get_dummy_lines():
    lines = ["str;in;g1", "s;tring;2", "string3", "string4"]
    return lines


def check_len_file(source_of_lines):
    lines = source_of_lines()
    print(len(lines))

    some_lines = get_some_lines(lines, 2)
    entries = create_entries(some_lines)
    print("number of entries: ", len(entries))
    print("display entries:", [entry.words for entry in entries])


def get_some_lines(lines, number_of_entries):
    return lines[0:number_of_entries]


def create_entries(lines):
    return [Entry(parse_file_line(line)) for line in lines]


def parse_file_line(line):
    return line.split(";")


class Entry:
    def __init__(self, words):
        # parse the line and turn it into the data
        self.words = words


if __name__ == '__main__':
    # check_len_file(get_file_lines)
    check_len_file(get_dummy_lines)
