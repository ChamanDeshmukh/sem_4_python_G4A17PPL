import socket

ip = '127.0.0.1'  
port = 48933  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip, port))

message = "Hello TCP server"
client.send(message.encode())

response = client.recv(1024)
print("Message from TCP server:", response.decode())

client.close()
