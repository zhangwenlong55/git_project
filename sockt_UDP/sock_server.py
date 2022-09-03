"""
UDP 服务端
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
s.bind(("localhost", 8000))

while True:
    msg, addr = s.recvfrom(1024)
    print(f"收到[{addr}]的消息:[{msg.decode()}]")
    s.sendto("已经收到您发送的消息".encode(), addr)  # UDP专用发消息方法,sendto
