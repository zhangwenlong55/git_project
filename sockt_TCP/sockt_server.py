"""
服务器端
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # step 1 初始化实例,ipv4或ipv6  ,TCP 或 UDP
s.bind(("0.0.0.0", 9000))  # step 2 (127.0.0.1只能本机访问),绑定IP + port
s.listen(2)  # step 3 允许挂起"2"个链接
client_conn, client_adr = s.accept()  # step 4 等待链接 , 当一个链接进来,就会为这个链接生成一个专属的实例

print("client_conn", client_conn, "client_adr", client_adr)

client_conn.send("Hello world, Study Python!!!".encode("u8"))  # 发数据，只能接受字节
date = client_conn.recv(1024)  # 收数据 ， 1024字节
print("客户端", date.decode("u8"))

client_conn.close()  # 关掉和客户端的链接

s.close()  # 关掉服务器
