import subprocess
import time
from threading import Thread

import tunnel_builder

LOOP_SYSLOG_FILENAME = {"SL": "/var/log/css_sl.log",
                        "ML": "/var/log/css_ml.log",
                        "LL": "/var/log/css_ll.log",
                        "SYS": "/var/log/syslog",
                        "TEST": "/home/renaud/test.txt"}


class Board:

    def __init__(self, remote, target):
        print "Fuck"
        self.address, self.port, self.tunnel = tunnel_builder.build_tunnel(remote, target)
        # self.__fs = fs.open_fs \
        #    ("ssh://%s:%s@%s:%d//" % (target.user, target.password, address, port))
        self.synchronized = File_Synchronizer()
        self.synchronized.run()

    def stop(self):
        if self.tunnel is not None:
            self.tunnel.stop()
        # self.synchronized.

    def get_loop_log(self, loop):
        return self.__fs.open(LOOP_SYSLOG_FILENAME[loop])


class File_Synchronizer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            print "pwet"
            subprocess.call("rsync renaud@server2:/var/log/syslog .", shell=True)
            time.sleep(1)
