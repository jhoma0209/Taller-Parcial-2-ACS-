
# 5. Crear un servidor que recoja los números que se envían desde el cliente y 
# devuelva la suma en el momento de enviar un cero.

# Creacion del servidor en Python

import socket

def start_server():
    # Crear un socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enlazar el socket al host y puerto
    server_socket.bind(('localhost', 12345))
    
    # Esperar conexiones entrantes (máximo 1 en cola)
    server_socket.listen(1)
    print("Servidor esperando conexión...")

    # Aceptar la conexión del cliente
    conn, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    total_sum = 0

    while True:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = conn.recv(1024).decode()
        num = int(data)
        
        if num == 0:
            # Enviar la suma total al cliente y cerrar la conexión
            conn.send(str(total_sum).encode())
            print("Suma total enviada. Cerrando conexión.")
            break
        else:
            total_sum += num
            print(f"Número recibido: {num}, suma parcial: {total_sum}")

    # Cerrar la conexión
    conn.close()

if __name__ == '__main__':
    start_server()
