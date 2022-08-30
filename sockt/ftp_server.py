"""
文件收发服务端
"""
import socket
import os

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # SOL_SOCKET SO_REUSEADDR 允许重用本地地址和端口

ser.bind(("localhost", 9001))
ser.listen(2)

count = 0
while True:
    conn, adr = ser.accept()
    count += 1
    print(f"[{count} - got connection :{adr}]")

    while True:
        cmd = conn.recv(1024).decode()
        if not cmd:
            print(f"{adr}断开连接")
            break
        print(f"from client {adr}:{cmd}")

        # step1 服务器端收到客户指令,解析 判断get开头,下载文件
        if cmd.startswith("get"):

            # step2 提取文件名,判断文件是否存在,如果存在的话就下载
            filename = cmd.split()[1]
            if os.path.isfile(filename):
                file_size = os.path.getsize(filename)

                # step3 生成消息偷发送给客户端
                msg_head = f"|{file_size}".zfill(32)
                conn.send(msg_head.encode())

                # 打开文件,发送文件内容
                with open(filename, "rb") as f:
                    for line in f:  # 循环每行发送,文件过大一次性读到内存容易撑爆
                        conn.send(line)
                    print(f"{filename} has send {adr},size :{file_size}")

        else:
            pass

ser.close()
