import json
from data_structures.datacenter import Datacenter

# Using the pytest module for developing unit tests
f = open(r'..\response.json')
data = json.load(f)
datacenters = [Datacenter(key, value) for key, value in data.items()]


def test_remove_invalid_clusters():
    # Verify that all the invalid clusters are removed and valid ones remain
    cluster_list = []
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            cluster_list.append(cluster.name)

    assert 'BER-1' in cluster_list, "Test failed, remove invalid clusters failed, entry should not be removed"
    assert 'BER-203' in cluster_list, "Test failed, remove invalid clusters failed, entry should not be removed"
    assert 'BER-4000' not in cluster_list, "Test failed, remove invalid clusters failed, entry should have been removed"
    assert 'TEST-1' not in cluster_list, "Test failed, remove invalid clusters failed, entry should have been removed"
    assert 'PAR-1' in cluster_list, "Test failed, remove invalid clusters failed, entry should not be removed"
    assert 'XPAR-2' not in cluster_list, "Test failed, remove invalid clusters failed, entry should have been removed"


def test_remove_invalid_records():
    # Verify that all the invalid addresses are removed and valid ones remain
    address_list = []
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                for address in network.entries:
                    address_list.append(address.address)

    assert '255.255.255.0' not in address_list, "Test failed, address should have been removed"
    assert '192.168..0.3' not in address_list, "Test failed, address should have been removed"
    assert '192.168.0' not in address_list, "Test failed, address should have been removed"
    assert '192.168.0.288' not in address_list, "Test failed, address should have been removed"
    assert 'invalid' not in address_list, "Test failed, address should have been removed"
    assert '192.168.1.1' not in address_list, "Test failed, address should have been removed"
    assert '10.0.10.a' not in address_list, "Test failed, address should have been removed"
    assert '192.168.0.0' not in address_list, "Test failed, address should have been removed"
    assert '192.168.0.1' in address_list, "Test failed, address should have not been removed"
    assert '192.168.0.2' in address_list, "Test failed, address should have not been removed"
    assert '192.168.0.3' in address_list, "Test failed, address should have not been removed"


def test_sort_records():
    # Verify that for a given network the addresses are sorted
    address_list = []
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                for address in network.entries:
                    address_list.append(address.address)
                break
            break
        break

    assert address_list == sorted(address_list), "Failed, the addresses are not sorted"
