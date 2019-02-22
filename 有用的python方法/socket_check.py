import socket


def socket_check(ipaddr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # s = socket.socket()
        s.settimeout(20)
        s.connect(ipaddr[1])
        s.shutdown(2)
        msg = ipaddr[0] + " http://" + str(ipaddr[1][0]) + ":" + str(ipaddr[1][1]) + " is healthy!"
        print(msg)
        return True
    except Exception as e:
        msg = ipaddr[0] + " http://" + str(ipaddr[1][0]) + ":" + str(ipaddr[1][1]) + " is unhealthy!"
        print(msg, e)
        return False
