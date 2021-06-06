class Cluster:
    def __init__(self, words):
        # parse the line and turn it into the data
        self.words = words

    def get_entry_description(self):
        # in other language it's possible to restrict direct access to the object's attributes
        # and do it through such a method instead
        return "words in this cluster:" + "| ".join(self.words)

    def has_common_words(self, other_cluster):
        return len([word for word in other_cluster.words if word in self.words]) > 0

    def get_number_words(self):
        return len(self.words)