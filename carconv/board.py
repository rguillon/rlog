import subprocess
import time
from threading import Thread

import tunnel_builder

LOOP_SYSLOG_FILENAME = {"SL": "/var/log/css_sl.log",
                        "ML": "/var/log/css_ml.log",
                        "LL": "/var/log/css_ll.log",
                        "SYS": "/var/log/syslog",
                        "TEST": "/home/renaud/test.txt"}

TEMP_FILES_DIR = "tmp"


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

    def __init__(self, target):
        Thread.__init__(self)
        self.target = target
        self.files = []

    def _sync_file(self, filename):
        subprocess.call("rsync %s:%s@%s:%s %s" % (self.target.user,
                                                  self.target.password,
                                                  self.target.address,
                                                  filename,
                                                  self._local_file_name(filename)), shell=True)

    def get_remote_file(self, filename):
        self._sync_file(filename)
        self.files.append(filename)
        return open(self._local_filename(filename))

    def _local_file_name(self, filename):
        return "%s/%s/%s" % (TEMP_FILES_DIR, self.target.address, filename)


    def run(self):
        while True:
            print "pwet"
            for filename in self.files:
                self._sync_file(file)
            time.sleep(1)
