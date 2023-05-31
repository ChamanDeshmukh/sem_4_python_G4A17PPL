import socket

ip = '127.0.0.1'  
port = 19580

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello UDP server"
udp_client_socket.sendto(message.encode(), (ip, port))

response, addr = udp_client_socket.recvfrom(1024)
print("Message from UDP server:", response.decode())

udp_client_socket.close()

