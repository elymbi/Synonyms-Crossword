from collections import namedtuple

from crossword3 import *


def get_dummy_lines():
    # lines = ["str;in;g1", "s;tring;2", "s;tring3", "string4"]
    lines = ["st;ring", "str;ing", "str;ing", "strin;g", "s;trin;g", "s;tring"]
    return lines


def check_len_file(source_of_lines):
    lines = source_of_lines()
    print(len(lines))

    some_lines = get_some_lines(lines, 2)
    clusters = create_entries(lines)
    thesaurus = Thesaurus(clusters)
    # print("number of clusters: ", len(clusters))
    # print("display clusters:\n" + '\n'.join([entry.get_entry_description() for entry in clusters]))
    # display_all_cluster_properties(clusters)
    cluster_unions = divide_all_clusters_into_unions(thesaurus)

    # print("num unions:", len(cluster_unions))
    # print("num clusters:",len(clusters))
    filtered_clusters = filter_unions_by_num_clusters(cluster_unions, 4)
    print("num unions with over 3 clusters:", len(filtered_clusters))
    display_unions(filtered_clusters)


def display_unions(unions):
    for union in unions:
        print(union.get_union_description())


def filter_unions_by_num_clusters(cluster_unions, num):
    return [u for u in cluster_unions if u.get_num_clusters() >= num]


def get_some_lines(lines, number_of_entries):
    return lines[0:number_of_entries]


def create_entries(lines):
    return [Cluster(parse_file_line(line)) for line in lines]


def parse_file_line(line):
    return line.split(";")


def display_all_cluster_properties(all_clusters):
    # for cluster in all_clusters:
    #    prop = calculate_cluster_properties(cluster, all_clusters)
    #    print_cluster_properties(prop)

    all_props = (calculate_cluster_properties(cluster, all_clusters) for cluster in all_clusters)

    for prop in all_props:
        print_cluster_properties(prop)


def calculate_cluster_properties(cluster, all_clusters):
    num_matching = get_num_connected_clusters(cluster, all_clusters)
    num_words = cluster.get_number_words()
    return ClusterProperties(num_words, num_matching)


def get_num_connected_clusters(cluster, all_clusters):
    return sum(cluster.has_common_words(c) for c in all_clusters) - 1


ClusterProperties = namedtuple("ClusterProperties", "num_words num_matching_clusters")


def print_cluster_properties(props):
    print(f"new cluster: {props.num_words} words and "
          f"{props.num_matching_clusters} connected clusters")


def divide_all_clusters_into_unions(thesaurus):
    all_unions = []
    # return uniouns
    while not thesaurus.is_empty() and len(all_unions) < 2000:
        len_thes = len(thesaurus.all_clusters)
        len_unions = len(all_unions)
        print("remaining words:", len_thes, ";num unions:", len_unions, ";total:", len_thes + len_unions)
        cluster = thesaurus.eject_cluster()
        sort_cluster(cluster, all_unions)
    return all_unions


def sort_cluster(cluster, all_unions):
    try:
        union_for_cluster = next(union for union in all_unions if union.matches_cluster(cluster))
        union_for_cluster.add_cluster(cluster)
    except:
        new_union = ClusterUnion()
        new_union.add_cluster(cluster)
        all_unions.append(new_union)


class Thesaurus:
    def __init__(self, all_clusters):
        # parse the line and turn it into the data
        self.all_clusters = all_clusters[:]

    def eject_cluster(self):
        return self.all_clusters.pop(0)

    def is_empty(self):
        return len(self.all_clusters) == 0


class ClusterUnion:
    def __init__(self):
        self.clusters = []

    def get_num_clusters(self):
        return len(self.clusters)

    def add_cluster(self, cluster):
        self.clusters.append(cluster)

    def matches_cluster(self, cluster):
        return next((True for c in self.clusters if c.has_common_words(cluster)), False)

    def get_union_description(self):
        return "NEW UNION:\n" + '\n'.join([('*' + cluster.get_entry_description()) for cluster in self.clusters])


class Cluster:
    def __init__(self, words):
        # parse the line and turn it into the data
        self.words = words

    def get_entry_description(self):
        # in other language it's possible to restrict direct access to the object's attributes
        # and do it through such a method instead
        return "words in this cluster:" + ", ".join(self.words)

    def has_common_words(self, other_cluster):
        return len([word for word in other_cluster.words if word in self.words]) > 0

    def get_number_words(self):
        return len(self.words)


if __name__ == '__main__':
    check_len_file(get_file_lines)
    # check_len_file(get_dummy_lines)
