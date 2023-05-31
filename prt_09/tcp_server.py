import socket

ip = '127.0.0.1'  
port = 48933  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))

server.listen(1)
print("TCP server is up and listening...")

conn, addr = server.accept()
print('TCP client connected:', addr)

data = conn.recv(1024)
print("Message from TCP client:", data.decode())

response = "Hello TCP client"
conn.send(response.encode())

conn.close()
server.close()
