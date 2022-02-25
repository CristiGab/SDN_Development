import ipaddress
import re
from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipv4_network
        self.entries = [Entry(entry['address'], entry['available'], entry['last_used']) for entry in raw_entry_list]

        self.remove_invalid_records()
        self.sort_records()

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        regex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)"
                           "{3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")

        self.entries = [valid_ip for valid_ip in self.entries
                        if regex.search(valid_ip.address) and
                        ipaddress.IPv4Address(valid_ip.address) in ipaddress.ip_network(self.ipv4_network)]

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
