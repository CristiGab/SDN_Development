import re
from data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = [Cluster(key, value['networks'], value['security_level'])
                         for key, value in cluster_dict.items()]

        self.remove_invalid_clusters()

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        regex = re.compile('^[A-Z]{3}-[0-9]{1,3}$')
        self.clusters = [valid_cluster for valid_cluster in self.clusters if regex.search(valid_cluster.name)]
