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