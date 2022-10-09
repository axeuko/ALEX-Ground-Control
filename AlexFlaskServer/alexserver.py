from alexpackages import ALEXSERVER
import socket


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)


if __name__ == "__main__":
    #ALEXSERVER.run(host = str(IPAddr), port = 80, debug = True)
    ALEXSERVER.run(host = '172.16.2.116', port = 80, debug = True)
