from crossword3 import *


def get_dummy_lines():
    lines = ["str;in;g1", "s;tring;2", "string3", "string4"]
    return lines


def check_len_file(source_of_lines):
    lines = source_of_lines()
    print(len(lines))

    some_lines = get_some_lines(lines, 2)
    clusters = create_entries(lines)
    # print("number of clusters: ", len(clusters))
    # print("display clusters:\n" + '\n'.join([entry.get_entry_description() for entry in clusters]))
    display_all_cluster_properties(clusters)


def get_some_lines(lines, number_of_entries):
    return lines[0:number_of_entries]


def create_entries(lines):
    return [Cluster(parse_file_line(line)) for line in lines]


def parse_file_line(line):
    return line.split(";")


def display_all_cluster_properties(all_clusters):
    [display_cluster_properties(cluster) for cluster in all_clusters]


def display_cluster_properties(cluster):
    print("new cluster words:", cluster.get_number_words(), "and number of connected clusters:", 0)


class Cluster:
    def __init__(self, words):
        # parse the line and turn it into the data
        self.words = words

    def get_entry_description(self):
        # in other language it's possible to restrict direct access to the object's attributes
        # and do it through such a method instead
        return "words in this cluster:" + ", ".join(self.words)

    def has_common_words(self, other_cluster):
        return [word for word in other_cluster.words if word in self.words]

    def get_number_words(self):
        return len(self.words)


if __name__ == '__main__':
    # check_len_file(get_file_lines)
    check_len_file(get_dummy_lines)
