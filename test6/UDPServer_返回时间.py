# 服务端

import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 5008))  # 绑定端口和端口号，空字符串表示本机任何可用IP地址
print("UDP开始")
while True:
    data, addr = s.recvfrom(1024)
    data = data.decode()
    print('received message:{0} from PORT {1[1]} on {1[0]}'.format(data, addr))
    Time = str(time.asctime(time.localtime(time.time())))
    s.sendto(Time.encode(), addr)
    if data.lower() == 'bye':
        break
s.close()
