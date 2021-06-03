from unittest import TestCase
from main import *

class TestCluster(TestCase):

    def test_get_entry_description(self):
        self.fail()

    def test_has_no_common_words(self):
        cluster1 = Cluster(["a","b","c","d","e","f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "eb", "fb"])
        self.assertFalse(cluster1.has_common_words(cluster2))

    def test_has_common_words(self):
        cluster1 = Cluster(["a","b","c","d","e","f"])
        cluster2 = Cluster(["ab", "bb", "cb", "db", "b", "fb"])
        self.assertTrue(cluster1.has_common_words(cluster2))
