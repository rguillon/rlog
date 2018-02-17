import time

from carconv.rack import Rack
from carconv.target import Target

rack = Rack(host=Target(address="server1", port=22, user="renaud", password="server1"),
            rack_address=None,
            boards={"A": Target(address="server2", port=22, user="renaud", password="server2"),
                    "B": Target(address="server2", port=22, user="renaud", password="server2")})

num = 0

syslogA = rack.get_board("A").get_loop_log("TEST")
syslogB = rack.get_board("B").get_loop_log("TEST")

while 1:
    # for line in syslogA:
    #    print line
    for line in syslogB:
        print "\"%s\"" % line
    time.sleep(1)

