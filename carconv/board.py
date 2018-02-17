import fs

import tunnel_builder

LOOP_SYSLOG_FILENAME = {"SL": "/var/log/css_sl.log",
                        "ML": "/var/log/css_ml.log",
                        "LL": "/var/log/css_ll.log",
                        "SYS": "/var/log/syslog.log",
                        "TEST": "/home/renaud/test.txt"}


class Board:

    def __init__(self, remote, target):
        address, port = tunnel_builder.build_tunnel(remote, target)
        self.__fs = fs.open_fs \
            ("ssh://%s:%s@%s:%d//" % (target.user, target.password, address, port))


    def get_loop_log(self, loop):
        return self.__fs.open(LOOP_SYSLOG_FILENAME[loop])
