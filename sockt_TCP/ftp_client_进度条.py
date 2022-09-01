"""
文件收发客户端,实现进度条打印, (需要完善)
"""
import socket
import time
from tqdm import tqdm

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("localhost", 9001))

while True:
    cmd = input("input cmd >>>:")
    if not cmd:
        continue
    if cmd == "q":
        break

    # 发送指令至服务器
    cli.send(cmd.encode())
    # 2. 接受固定长度消息头
    msg_head = cli.recv(32).decode()
    # 3. 拿到文件大小和文件名
    file_size = int(msg_head.split("|")[1])
    file_name = cmd.split()[1]
    # 4. 在本地创建一个文件 .download
    with open(f"{file_name}.download", "wb") as f:
        # 5 . 循环接受数据
        receive_size = 0
        start = time.time()
        while receive_size < file_size:
            d = cli.recv(1024)
            receive_size += len(d)  # 不断地更新已经收到了多少
            f.write(d)
            # # print(file_size, receive_size)
        # for i in tqdm(iterable=range(file_size), total=file_size, desc="正在传输"):
        #     pass

        print(file_size, receive_size)

        print(f"file download done size :{file_size},time :{time.time() - start}s")

cli.close()
