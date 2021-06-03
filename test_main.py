from unittest import TestCase
from main import *


class TestCluster(TestCase):

    def test_has_no_common_words(self):
        cluster1 = Cluster(["a", "b", "c", "d", "e", "f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "eb", "fb"])
        self.assertFalse(cluster1.has_common_words(cluster2))

    def test_has_common_words(self):
        cluster1 = Cluster(["a", "b", "c", "d", "e", "f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "b", "fb"])
        self.assertTrue(cluster1.has_common_words(cluster2))

    def test_how_many_connected_clusters(self):
        cluster1 = Cluster(["a", "b", "c", "d", "e", "f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "b", "fb"])
        self.assertEqual(1, get_num_connected_clusters(cluster1, [cluster1, cluster2]))

    def test_no_connected_clusters(self):
        cluster1 = Cluster(["a", "b", "c", "d", "e", "f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "bb", "fb"])
        self.assertEqual(0, get_num_connected_clusters(cluster1, [cluster1, cluster2]))


class TestClusterUnion(TestCase):
    def test_matches_cluster(self):
        cluster1 = Cluster(["a", "b", "c", "d", "e", "f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "b", "fb"])
        union = ClusterUnion()
        union.add_cluster(cluster1)
        union.add_cluster(cluster2)
        self.assertTrue(union.matches_cluster(cluster1))

    def test_does_not_match_cluster(self):
        cluster1 = Cluster(["a", "b", "c", "d", "e", "f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "b", "fb"])
        union = ClusterUnion()
        union.add_cluster(cluster1)
        self.assertTrue(union.matches_cluster(cluster2))

