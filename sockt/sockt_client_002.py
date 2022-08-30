"""
客户端循环收发消息
"""
import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost",6000))

while True:
    msg = input("输出信息：").strip()
    if not msg:
        continue
    if msg == "q":
        break
    cli.send(msg.encode())

    res = cli.recv(1024)
    print(f"from server:{res.decode()}")

cli.close()
