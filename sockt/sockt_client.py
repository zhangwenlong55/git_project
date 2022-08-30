"""
客户端
"""
import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9000))

data = cli.recv(1024)  # 最大收1024
print("服务器端", data.decode("u8"))

cli.send("干嘛呢,我在学习如何使用网络编程".encode("u8"))

cli.close()
