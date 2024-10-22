import threading  # Librería que permite crear y manejar hilos.
import time  # Librería para medir el tiempo de ejecución.

class AreaCalculator:
    def __init__(self):
        self.areas = {}  # Diccionario que almacenará las áreas calculadas de las figuras geométricas.

    def area_triangulo(self, base, altura, shape_name):
        #print(f"Calculando área del {shape_name}")  # Depuración
        area = (base * altura) / 2  # Fórmula para calcular el área de un triángulo.
        self.areas[shape_name] = area  # Almacena el área calculada en el diccionario con su respectivo nombre.

    def area_rectangulo(self, base, altura, shape_name):
        #print(f"Calculando área del {shape_name}")  # Depuración
        area = base * altura  # Fórmula para calcular el área de un rectángulo.
        self.areas[shape_name] = area  # Almacena el área calculada en el diccionario con su respectivo nombre.

def draw_figure():
    # Imprime una representación visual de la figura geométrica.
    figure = [
        "          /|---------------|",
        "         /        8m       |",
        "        /  |               |",
        "       /                   |",
        "      /    |               |",
        "     /                     |",
        "    /      |  12m          |   6m ",
        "   /                       |---------\\",
        "  /        |                        | \\",
        " /                              5m     \\",
        "/  10m     |                            \\",
        "------------------------------------|----\\",
        "|  ------------     26m     --------------|"
    ]
    for line in figure:
        print(line)  # Imprime cada línea que representa la figura geométrica.

def calcular_area_total():
    calculator = AreaCalculator()  # Crear una instancia de la clase AreaCalculator.

    # Crear los hilos para cada área
    hilos = []
    hilos.append(threading.Thread(target=calculator.area_triangulo, args=(10, 12, "Triángulo Izquierdo")))  # Triángulo izquierdo
    hilos.append(threading.Thread(target=calculator.area_rectangulo, args=(8, 12, "Rectángulo Central")))  # Rectángulo central
    hilos.append(threading.Thread(target=calculator.area_rectangulo, args=(6, 5, "Rectángulo Derecho")))   # Rectángulo derecho
    hilos.append(threading.Thread(target=calculator.area_triangulo, args=(2, 5, "Triángulo Derecho")))     # Triángulo derecho pequeño

    # Medir tiempo de ejecución
    start_time = time.time()  # Guarda el tiempo de inicio.

    # Iniciar los hilos
    for hilo in hilos:
        #print(f"Iniciando hilo {hilo}")  # Depuración
        hilo.start()  # Inicia cada hilo para calcular las áreas de manera concurrente.

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()  # Espera a que cada hilo finalice su ejecución.
        #print(f"Hilo {hilo} ha terminado")  # Depuración

    end_time = time.time()  # Guarda el tiempo de fin.

    # Dibujar la figura geométrica
    print("\nFigura geométrica:")
    draw_figure()  # Llama a la función que imprime la figura en la terminal.

    # Calcular y mostrar los resultados
    print("\nResultados:")
    print("-" * 40)  # Imprime una línea separadora.
    for shape, area in calculator.areas.items():
        print(f"Área de {shape}: {area:.2f} m²")  # Imprime el área de cada figura almacenada en el diccionario.

    total_area = sum(calculator.areas.values())  # Suma las áreas de todas las figuras.
    print(f"\nÁrea total: {total_area:.2f} m²")  # Imprime el área total de la figura.
    print(f"Tiempo de ejecución: {(end_time - start_time):.4f} segundos")  # Imprime el tiempo que tomó ejecutar todo el cálculo.

# Ejecutar el cálculo
calcular_area_total()
