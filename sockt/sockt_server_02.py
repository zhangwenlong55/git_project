"""
服务器端,实现多次收发信息
"""
import socket

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(("0.0.0.0", 6000))
ser.listen(2)  # 允许两人排队
count = 0

while True:  # 为了不断的接受新链接
    conn, addr = ser.accept()  # 等待连接
    count += 1
    print(f"[{count}]got a new connection {addr}")

    while True:  # 为了不断的收发数据
        data = conn.recv(1024)  # 阻塞
        if not data:
            print(f"{addr}断开连接")
            break
        print(f"from client{addr}:{data.decode()}")
        conn.send(f"already received:{data.decode()}".encode())

ser.close()
