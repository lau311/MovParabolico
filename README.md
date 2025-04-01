# Simulador de Movimiento Parabólico
![Ejemplo de Movimiento parabólico](https://ingenierizando.com/wp-content/uploads/2023/02/movimiento-parabolico.png?raw=true)
## Descripción
Este proyecto es una simulación del **movimiento parabólico** de un proyectil en 2D, considerando la **aceleración gravitatoria**. Implementa una estructura **orientada a objetos** con clases que representan objetos físicos y vectores bidimensionales.  

Además, incluye una función de aproximación de la función **arctan** mediante la **serie de Taylor**. Al ejecutar el programa, el usuario ingresa las condiciones iniciales y la simulación calcula la trayectoria hasta que el proyectil toca el suelo.

## Características
✔️ Simulación del movimiento parabólico de un proyectil.  
✔️ Cálculo de **alcance horizontal** y **altura máxima**.  
✔️ Cálculo del **ángulo de lanzamiento** utilizando la serie de **Taylor**.  
✔️ Representación **gráfica** de la trayectoria.  
✔️ Implementación con **Programación Orientada a Objetos (POO)**.  

## Fundamentos Matemáticos

El movimiento parabólico de un proyectil se describe mediante las siguientes ecuaciones:

### Posición en función del tiempo:
$$
x(t) = x_0 + v_{0x} t
$$
$$
y(t) = y_0 + v_{0y} t - \frac{1}{2} g t^2
$$

### Velocidad en función del tiempo:
$$
v_x = v_{0x}
$$
$$
v_y = v_{0y} - g t
$$

### Tiempo de vuelo:
$$
t_f = \frac{2 v_{0y}}{g}
$$

### Alcance horizontal:
$$
R = v_{0x} t_f
$$

### Altura máxima:
$$
h_{\max} = \frac{v_{0y}^2}{2g}
$$

### Aproximación del **arctan(x)** usando la **serie de Taylor**:
$$
\arctan(x) \approx \sum_{n=0}^{N} (-1)^n \frac{x^{2n+1}}{2n+1}
$$

## Requisitos
- **Python**
- Librerías necesarias:
  - `matplotlib`
  - `math`

