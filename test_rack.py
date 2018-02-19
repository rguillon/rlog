from __future__ import print_function

import time

from carconv.rack import Rack
from carconv.target import Target

rack = Rack(host=Target(address="localhost", port=22, user="renaud", password="server1"),
            rack_address=None,
            boards={"A": Target(address="server2", port=22, user="renaud", password="server2")})

#  "B": Target(address="server2", port=22, user="renaud", password="server2")})

time.sleep(1)
rack.stop()
