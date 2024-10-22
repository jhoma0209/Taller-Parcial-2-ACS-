
# 4. Generar un programa servidor que responda con el número de vocales 
# que tiene la cadena que se va a enviar después.

# Creacion del servidor en Python

import socket

def contar_vocales(cadena):
    """
    Función que cuenta el número de vocales en una cadena.
    Vocales consideradas: a, e, i, o, u (minúsculas y mayúsculas).
    """
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

def iniciar_servidor():
    """
    Función que inicializa el servidor. 
    Escucha conexiones en el puerto 65432 y responde con el número de vocales en la cadena recibida.
    """
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 65432))
    servidor.listen()
    print("Servidor escuchando en el puerto 65432...")

    while True:
        try:
            conexion, direccion = servidor.accept()
            print(f"Conexión establecida con {direccion}")

            while True:
                # Recibe datos del cliente
                datos = conexion.recv(1024).decode('utf-8')  # Sin strip() por ahora
                if not datos:
                    print("No se recibieron datos. Cerrando conexión.")
                    break  # Salir del bucle si no hay datos

                # Comprobar si el cliente quiere cerrar la conexión
                if datos.strip().lower() == "exit":
                    print("Cliente ha solicitado cerrar la conexión.")
                    break  # Salir del bucle si el cliente quiere cerrar                    
               
                print(f"Cadena recibida: {datos}")

                # Contar el número de vocales en la cadena recibida
                num_vocales = contar_vocales(datos)
                
                # Responder al cliente con el número de vocales
                respuesta = f"El número de vocales es: {num_vocales}\n"  # Añadir nueva línea al final
                conexion.sendall(respuesta.encode('utf-8'))

        except Exception as e:
            print(f"Error en la conexión: {e}")
            break  # Salir del bucle en caso de error

        finally:
            # Cerrar la conexión con el cliente
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    iniciar_servidor()
