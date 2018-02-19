import auto_rsync

sync = auto_rsync.main(".", "renaud@server1:/var/log/syslog", "10", " ")
