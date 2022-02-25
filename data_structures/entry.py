import datetime
import ipaddress


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = datetime.datetime.strptime(last_used, '%d/%m/%y %H:%M:%S')

    def __lt__(self, other):
        return ipaddress.IPv4Address(self.address) < ipaddress.IPv4Address(other.address)
