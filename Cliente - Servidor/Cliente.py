import socket

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección IP y puerto del servidor al que conectarse
host = '127.0.0.1'
port = 12345

# Conectar con el servidor
client_socket.connect((host, port))

# Enviar un mensaje al servidor
message = "Hola servidor!"
client_socket.send(message.encode('utf-8'))

# Recibir la respuesta del servidor
data = client_socket.recv(1024).decode('utf-8')
print(f"Respuesta del servidor: {data}")

# Cerrar el socket del cliente
client_socket.close()
