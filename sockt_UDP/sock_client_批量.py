"""
UDP 客户端
"""
import socket
import time
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    c.sendto("Hello world!!!".encode(), ("localhost", 8000))   # 客户端不启动不会报错
    # data, addr = c.recvfrom(1024)
    # print(data.decode(), addr)
    time.sleep(0.2)
