#Hay un error en el código, marcado en el lugar donde corresponde. Corregir 
import math

# se define la función que representa la EDO del ejercicio 1
def f_1(x, y):
    return 0.2 * x * y

# ahora con el ejercico 2
def f_2(t, I):
    return 15 - 3 * I

# se define la solucion exacta de la EDO del ejercicio 1
def solucion_exacta_1(x):
    return math.exp(0.1 * x**2 - 0.5) #chequear esta solución

# ahora con el ejercicio 2 
def solucion_exacta_2(t):
    return 5 - 5 * math.exp(-3 * t)

# Implementacion del método de Euler
def metodo_de_euler(f, y0, t0, tn, h):
    t = t0
    y = y0
    while t < tn:
        y = y + h * f(t, y)
        t += h
    return y

# se define  los parámetros del problema 1
y0_1 = 1.0
t0_1 = 1.0
tn_1 = 1.5

# lo mismo con el problema 2
I0_2 = 0.0
t0_2 = 0.0
tn_2 = 0.5

# Calculamos la solucion exacta del problema 1
solucion_exacta_at_1_5 = solucion_exacta_1(tn_1)

# Calculamos la solucion exacta del problema 2
solucion_exacta_at_0_5 = solucion_exacta_2(tn_2)

# con un paso de 0.1
h = 0.1
aproximacion_1 = metodo_de_euler(f_1, y0_1, t0_1, tn_1, h)
error_1 = abs(solucion_exacta_at_1_5- aproximacion_1)

# con un paso de 0.05
h = 0.05
aproximacion_2 = metodo_de_euler(f_1, y0_1, t0_1, tn_1, h)
error_2 = abs(solucion_exacta_at_1_5 - aproximacion_2)

#  problema 2 usando el método de Euler con un paso de 0.1
h = 0.1
aproximacion_3 = metodo_de_euler(f_2, I0_2, t0_2, tn_2, h)
error_3 = abs(solucion_exacta_at_0_5 - aproximacion_3)

# problema 2 usando el método de Euler con un paso de 0.05
h = 0.05
aproximacion_4 = metodo_de_euler(f_2, I0_2, t0_2, tn_2, h)
error_4 = abs(solucion_exacta_at_0_5 - aproximacion_4)

print("Resultados para el ejercicio 1:")
print(f"Solución exacta en t=1.5: {solucion_exacta_at_1_5}")
print(f"Aproximación con h=0.1: {aproximacion_1}, Error: {error_1}")
print(f"Aproximación con h=0.05: {aproximacion_2}, Error: {error_2}")

print("\nResultados para el ejercicio 2:")
print(f"Solución exacta en t=0.5: {solucion_exacta_at_0_5}")
print(f"Aproximación con h=0.1: {aproximacion_3}, Error: {error_3}")
print(f"Aproximación con h=0.05: {aproximacion_4}, Error: {error_4}")

