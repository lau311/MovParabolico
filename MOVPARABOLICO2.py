import matplotlib.pyplot as plt  # Librería para graficar
import math  # Librería matemática para cálculos
from abc import ABC, abstractmethod  # Módulo para definir clases abstractas

# Clase base abstracta para objetos físicos: permite que otraas clases hereden de objetofisico y reutilicen codigo
class ObjetoFisico(ABC):  #es una clase abstracta que representa cualquier objeto físico con posicion y velocidad.
    def __init__(self, posicion, velocidad): #init para los atributos del objeto
        self.posicion = posicion  # Posición del objeto en el espacio
        self.velocidad = velocidad  # Velocidad del objeto
    
    @abstractmethod
    def actualizar(self, tiempo):
        pass  # indica que el método no tiene código aún, pero es obligatorio que las subclases lo implementen.

# Clase para representar vectores en 2D
class Vector:
    def __init__(self, x, y):
        self._x = x  # Coordenada x del vector encapsulado
        self._y = y  # Coordenada y del vector encapsulado

    @property
    def x(self):
        return self._x  # Getter(permite obtener un valor de un atributo encapsulado) para obtener la coordenada x

    @property
    def y(self):
        return self._y  # Getter para obtener la coordenada y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)  # Suma de vectores

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)  # Multiplicación por escalar

# Clase para simular el movimiento de un proyectil
class ProjectileSimulator(ObjetoFisico):
    def __init__(self, initial_position, initial_velocity, gravity):
        super().__init__(initial_position, initial_velocity)  # Hereda de ObjetoFisico
        self.gravity = gravity  # Define la aceleración gravitatoria
        self.positions = []  # Lista para almacenar las posiciones durante la simulación
    
    def actualizar(self, time_step):# Define el método actualizar.
        gravity_force = Vector(0, -self.gravity)  # Vector de gravedad 
        delta_velocity = gravity_force * time_step  # Cambio de velocidad debido a la gravedad
        self.velocidad = self.velocidad + delta_velocity  # velocidad del proyectil en funcion del tiempo
        displacement = self.velocidad * time_step  # Cálculo del desplazamiento d=v*t. cuanto se movio el proyectil 
        self.posicion = self.posicion + displacement  # posicion del proyectil en el espacio
        self.positions.append((self.posicion.x, self.posicion.y))  # Almacenar la posición actual, y permite graficar despues.
        return self.posicion  # Retornar la nueva posición

# Función para calcular arctan mediante la serie de Taylor
def arctan_taylor(x, n=15): #Define una función llamada arctan_taylor, que toma dos parámetros
    if abs(x) <= 1: #si se cumple esta condición, se usa la expansión en serie.
        result = 0  # Inicializa la variable result, que almacenará el valor de la aproximación de arctan(x).
        sign = 1  # Variable para alternar los signos de la serie
        for i in range(1, 2 * n, 2):  # Se usa un for para iterar sobre los n primeros términos impares
            result += sign * (x ** i) / i  # Agregar término de la serie
            sign *= -1  # Cambiar el signo de cada iteracion
        return result  # se devuelve el valor aproximado de arctan(x).
    else:
        return math.atan(x)  # Usar la función atan de math si x es grande

# Solicitar al usuario los datos para la simulación
initial_position_x = float(input("Ingrese la coordenada x de la posición inicial: "))  # Entrada de x inicial
initial_position_y = float(input("Ingrese la coordenada y de la posición inicial: "))  # Entrada de y inicial
initial_velocity_x = float(input("Ingrese la coordenada x de la velocidad inicial: "))  # Entrada de velocidad en x
initial_velocity_y = float(input("Ingrese la coordenada y de la velocidad inicial: "))  # Entrada de velocidad en y

# Crear objetos Vector para posición y velocidad inicial: Esta sección define y almacena la posición y velocidad inicial del proyectil utilizando la clase Vector,
#  además de establecer la gravedad
initial_position = Vector(initial_position_x, initial_position_y)
initial_velocity = Vector(initial_velocity_x, initial_velocity_y)
gravity = 9.8  # Definir la aceleración gravitatoria en m/s²

# Crear instancia de la simulación
simulator = ProjectileSimulator(initial_position, initial_velocity, gravity)
#Se crea la simulación con la posición, velocidad y gravedad.
time_step = 0.01  # Se usa para calcular velocidad, desplazamiento y posición en cada iteración.
while True: #se usa while True porque no sabemos cuántas iteraciones serán necesarias hasta que el proyectil toque el suelo
    current_position = simulator.actualizar(time_step)  # Actualizar la simulación
    if current_position.y < 0: 
        break    # Detiene el ciclo (break) cuando la coordenada y es menor que 0 (cuando el proyectil toca el suelo).

# Extraer coordenadas x e y de las posiciones almacenadas
x_positions = [pos[0] for pos in simulator.positions] #extrae y guarda todas las coordenadas x en una lista
y_positions = [pos[1] for pos in simulator.positions] #lo mismo pero para las y 

# Calcular el alcance horizontal y la altura máxima
horizontal_range = max(x_positions) - min(x_positions)
vertical_range = max(y_positions) - min(y_positions)

# Mostrar resultados en consola
print(f"Alcance horizontal: {horizontal_range:.2f} metros")  # Mostrar alcance horizontal
print(f"Alcance vertical: {vertical_range:.2f} metros")  # Mostrar altura máxima

# Calcular el ángulo inicial de lanzamiento
angle_rad = arctan_taylor(initial_velocity_y / initial_velocity_x)  # calcula la pendiente de la trayectoria del proyectil en el punto de lanzamiento.
#en radianes
angle_deg = angle_rad * (180 / math.pi)  # Convertir de radianes a grados
print(f"Ángulo de tiro: {angle_deg:.2f} grados")  # Mostrar ángulo inicial

# Graficar la trayectoria del proyectil
plt.plot(x_positions, y_positions)
plt.title("Simulación de Movimiento Parabólico")  # Título del gráfico
plt.xlabel("Posición en x (metros)")  # Etiqueta del eje x
plt.ylabel("Posición en y (metros)")  # Etiqueta del eje y
plt.grid(True)  # Mostrar la cuadrícula en la gráfica
plt.show()  # Mostrar el gráfico
