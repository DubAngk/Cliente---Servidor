import socket

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# El servidor se enlaza a una IP y un puerto
host = '127.0.0.1'  # Dirección de loopback para pruebas locales
port = 12345        # Puerto del servidor

server_socket.bind((host, port))

# Configurar el servidor para que escuche conexiones entrantes
server_socket.listen(5)  # Permite hasta 5 conexiones

print(f"Servidor escuchando en {host}:{port}...")

while True:
    # Acepta una conexión
    client_socket, addr = server_socket.accept()
    print(f"Conexión establecida desde {addr}")
    
    # Recibe datos del cliente (1024 bytes a la vez)
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Mensaje del cliente: {data}")

    # Envía una respuesta al cliente
    message = "Mensaje recibido"
    client_socket.send(message.encode('utf-8'))
    
    # Cerrar la conexión con el cliente
    client_socket.close()

# Cerrar el socket del servidor
server_socket.close()
