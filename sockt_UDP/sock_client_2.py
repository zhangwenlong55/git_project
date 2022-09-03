"""
UDP 客户端
"""
import socket
import time
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    c.sendto("我是谁,我在哪儿????".encode(), ("localhost", 8000))
    data, addr = c.recvfrom(1024)
    print(data.decode(), addr)
    time.sleep(0.2)