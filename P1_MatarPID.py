# 1. Crear un programa que liste los procesos del sistema con su PID, 
# y permita eliminar uno que indiquemos.

# El PID (Process ID o Identificador de Proceso) es un número único asignado 
# por el sistema operativo a cada proceso en ejecución. Los procesos son programas que se están ejecutando,
# y el PID permite al sistema gestionar cada uno de manera individual.

# Uso de Módulo psutil para listar los procesos con su PID y para eliminar un proceso específico. 


# Importamos los módulos necesarios
import psutil  # Módulo para obtener información sobre los procesos del sistema
import os  # Módulo para interactuar con el sistema operativo

# Función que lista los procesos en ejecución
def listar_procesos():
    procesos = []  # Lista vacía para almacenar los procesos
    # Iteramos sobre todos los procesos en ejecución con psutil
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Añadimos a la lista un diccionario con la información del proceso: PID y nombre
            procesos.append(proc.info)
        except psutil.NoSuchProcess:
            # Capturamos la excepción en caso de que el proceso ya no exista
            pass
    return procesos  # Devolvemos la lista de procesos

# Función que elimina un proceso dado su PID
def eliminar_proceso(pid):
    try:
        # Intentamos eliminar el proceso con os.kill(), usando la señal 9 (SIGKILL)
        os.kill(pid, 9)
        print(f"Proceso con PID {pid} eliminado exitosamente.")  # Mensaje de éxito
    except ProcessLookupError:
        # Si no se encuentra un proceso con ese PID, mostramos un mensaje de error
        print(f"No se encontró un proceso con PID {pid}.")
    except PermissionError:
        # Si no tenemos permisos para eliminar el proceso, mostramos un mensaje de error
        print(f"No tienes permiso para eliminar el proceso con PID {pid}.")

# Bloque principal del programa
if __name__ == "__main__":
    # Imprimimos un encabezado para mostrar los procesos
    print("Procesos en ejecución:")
    # Llamamos a la función listar_procesos y mostramos cada proceso con su PID y nombre
    for proceso in listar_procesos():
        print(f"PID: {proceso['pid']} - Nombre: {proceso['name']}")
    
    # Solicitamos al usuario el PID del proceso que desea eliminar
    pid_a_eliminar = int(input("\nIngresa el PID del proceso a eliminar: "))
    
    # Llamamos a la función eliminar_proceso pasando el PID ingresado por el usuario
    eliminar_proceso(pid_a_eliminar)
