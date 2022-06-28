import socket  # 导入 socket 模块
s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号
s.connect((host, port))
while True:
    words = input('client:')
    s.send(words.encode())
    if words == 'byby':
        break
    mesg = s.recv(1024).decode()
    print('server:', mesg)
    if mesg == 'byby':
        break
print('connect break')
s.close()
