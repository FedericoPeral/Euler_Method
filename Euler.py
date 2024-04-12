#Hay dos errores en el código que están marcados donde corresponde. Faltaría comprobar los resultados usando la solución obtenida por 
#métodos algebraicos, y el cálculo del error. Después comentame en clase si te diste cuenta de los errores y pudiste completar el código.
#Me faltó comentar que podés subirlo al campus (o colocá un texto diciendo que ya está, así lo califico)
import numpy as np

def euler(f, x0, y0, x_end, n):
    """
    Implementa el método de Euler para resolver un problema de valor inicial.

    Parámetros:
    f (función): La función que representa la ecuación diferencial.
    x0 (float): El valor inicial de la variable independiente.
    y0 (float): El valor inicial de la variable dependiente.
    x_end (float): El valor final de la variable independiente.
    n (int): El número de pasos a utilizar.

    Retorna:
    np.ndarray: Un vector que contiene los valores aproximados de la variable dependiente.
    """
    h = (x_end - x0) / n
    x = np.linspace(x0, x_end, n + 1)
    y = np.zeros_like(x)
    y[0] = y0

    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])

    return y, x

def main():
    print("Método de Euler para problemas de valor inicial")

    # Ejercicio 1
    def f1(x, y):
        return 0.2 * x * y

    y1, x1 = euler(f1, 1, 1, 1.5, 10)
    print("Ejercicio 1:")
    print(f"Usando un paso de 0.1: y(1.5) = {y1[-1]:.4f}")

    y2, x2 = euler(f1, 1, 1, 1.5, 20)
    print(f"Usando un paso de 0.05: y(1.5) = {y2[-1]:.4f}")

    # Ejercicio 2
    def f2(t, I):
        R = 12
        L = 4
        V = 60
        return (V - 3 * I) / L #hay un error en la función introducida

    I, t = euler(f2, 0, 0, 0.5, 100) #para respetar el tamaño de paso pedido, modificar el número de pasos 
    print("\nEjercicio 2:")
    print(f"La corriente en el circuito medio segundo después de cerrar el interruptor es: I(0.5) = {I[-1]:.4f} A")

if __name__ == "__main__":
    main()
