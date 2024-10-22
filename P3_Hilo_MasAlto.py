
#3. programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números aleatorios entre el 1 y el 1000. Muestre el resultado de cada hilo. Ganará el hilo que consiga el número más alto.

import threading  # Importa el módulo threading para trabajar con hilos.
import random     # Importa el módulo random para generar números aleatorios.

# Función que será ejecutada por cada hilo.
# Recibe el identificador del hilo y la lista compartida donde se almacenan los resultados.

print ("\t 100 números aleatorios entre 1 y 1000 y se suman \t")

def sumar_numeros(hilo_id, resultados):
    # Genera 100 números aleatorios entre 1 y 1000 y los suma.
    suma = sum(random.randint(1, 1000) for _ in range(100))
    
    # Almacena el resultado (la suma) en la posición correspondiente de la lista 'resultados'.
    resultados[hilo_id] = suma
    
    # Imprime el resultado del hilo actual.
    print(f"Hilo {hilo_id} suma: {suma}")

# Función principal para crear y ejecutar los hilos.
def ejecutar_hilos():
    num_hilos = 10  # Número de hilos a crear.
    
    # Lista para almacenar los resultados de cada hilo (una posición para cada hilo).
    # Inicialmente, se llena con ceros.
    resultados = [0] * num_hilos
    
    # Lista para almacenar las referencias de los hilos que se crearán.
    hilos = []

    
    
    # Crear y lanzar cada uno de los 10 hilos.
    for i in range(num_hilos):
        # Crea un nuevo hilo, asignándole la función 'sumar_numeros' y pasándole
        # como argumentos el identificador del hilo (i) y la lista de resultados.
        hilo = threading.Thread(target=sumar_numeros, args=(i, resultados))
        
        # Añade el hilo a la lista 'hilos' para poder controlarlo más tarde.
        hilos.append(hilo)
        
        # Inicia la ejecución del hilo.
        hilo.start()

    # Espera que todos los hilos terminen antes de continuar.
    for hilo in hilos:
        # 'join()' bloquea la ejecución del programa principal hasta que este hilo termine.
        hilo.join()
        
    print ("\t\t Resultados obtenidos por cada hilo. \t")
        
    # Mostrar los resultados obtenidos por cada hilo.
    for i, resultado in enumerate(resultados):
        # Imprime el número del hilo y la suma que calculó.
        print(f"Hilo {i} total: {resultado}")

    # Determinar el hilo ganador, es decir, el que tiene la suma más alta.
    # La función 'max(resultados)' devuelve la suma más alta,
    # y 'resultados.index(max(resultados))' devuelve el índice de ese resultado.
    hilo_ganador = resultados.index(max(resultados))
    
    # Imprime cuál fue el hilo ganador y su suma.
    print(f"\nEl hilo {hilo_ganador} ganó con una suma de {resultados[hilo_ganador]}")

# Ejecuta la función principal si este archivo es el programa principal (es decir, no es importado como módulo).
if __name__ == "__main__":
    ejecutar_hilos()


# los números que se obtienen son bastante altos porque el rango de los números aleatorios que se estan sumando es de 1 a 1000. Al sumar 100 números aleatorios entre 1 y 1000, es natural que se obtenga sumas altas.