import socket

ip = '127.0.0.1'  
port = 19580 

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_server_socket.bind((ip, port))
print("UDP server is up and listening...")

data, addr = udp_server_socket.recvfrom(1024)
print("Message from UDP client:", data.decode())

response = "Hello UDP client"
udp_server_socket.sendto(response.encode(), addr)

udp_server_socket.close()
