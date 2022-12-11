import socket
import threading


def portScanner(host, port):
    socket.setdefaulttimeout(0.5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("port", port, " open/tcp")
        s.close()
    except:
        return


for p in range(0, 65536):
    my_thread = threading.Thread(
        target=portScanner, args=("60.205.212.22", p))
    my_thread.start()
