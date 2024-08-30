from socket import *
import os

myHost = '127.0.0.1'
myPortNumber = 8000

# Configurando o servidor
server = socket(AF_INET, SOCK_STREAM)
server.bind((myHost, myPortNumber))
server.listen(1)

print("Servidor iniciado...")
print("Servidor na porta:", myPortNumber)
print("Servidor no endereço:", myHost)

try:
    while True:
        connection, address = server.accept()
        print('Servidor conectado por', address)

        request = connection.recv(1024).decode('utf-8')
        print("Requisição recebida:", request)

        messageTemp = request.split(' ')
        if len(messageTemp) > 1:
            messageFile = messageTemp[1][1:] 
            
            if messageFile == '':
                messageFile = 'index.html'

            try:
                with open(messageFile, 'rb') as file:
                    response = file.read()

                if messageFile.endswith('.html'):
                    tipoarquivo = 'text/html'
                elif messageFile.endswith('.txt'):
                    tipoarquivo = 'text/plain'
                else:
                    tipoarquivo = 'application/octet-stream'  

                header = 'HTTP/1.1 200 OK\n'
                header += 'Content-Type: ' + tipoarquivo + '\n\n'

            except Exception as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = '<html><meta charset="utf-8"><body><center><h3>Erro 404: Arquivo não encontrado</h3>' \
                           '<p>Servidor Python</p></center></body></html>'.encode('utf-8')

        respostafinal = header.encode('utf-8')
        respostafinal += response                    
        connection.send(respostafinal)                  
        connection.close()

except KeyboardInterrupt:
    print("\nServidor encerrado pelo usuário.")

finally:
    server.close()
    print(f"Porta {myPortNumber} liberada. Servidor fechado.")
