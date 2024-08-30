import socket

HOST = '127.0.0.1'
PORT = 65432   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    s.sendall('Ola, servidor'.encode('utf-8')) 
    data = s.recv(1024)  

print(f'Recebido do servidor: {data.decode()}')
