
# Creacion del cliente

import socket

def start_client():
    # Crear un socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectar al servidor
    client_socket.connect(('localhost', 12345))

    while True:
        # Solicitar un número al usuario
        num = input("Ingresa un número (0 para obtener la suma): ")
        
        # Enviar el número al servidor
        client_socket.send(num.encode())

        if int(num) == 0:
            # Recibir la suma del servidor
            total_sum = client_socket.recv(1024).decode()
            print(f"Suma total recibida del servidor: {total_sum}")
            break

    # Cerrar la conexión
    client_socket.close()

if __name__ == '__main__':
    start_client()
