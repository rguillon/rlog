import sshtunnel

port = 10000


def build_tunnel(remote, target):
    global port

    ret = []
    if 'localhost' in remote.address:
        ret = target.address, target.port, None
    else:
        port += 1
        forwarder = sshtunnel.SSHTunnelForwarder(
            ssh_address_or_host=(remote.address, remote.port),
            ssh_username=remote.user,
            ssh_password=remote.password,
            remote_bind_address=(target.address, target.port),
            local_bind_address=('127.0.0.1', port))
        forwarder.start()
        ret = '127.0.0.1', port, forwarder
    return ret
