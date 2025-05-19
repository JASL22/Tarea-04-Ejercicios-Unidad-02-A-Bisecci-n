import numpy as np

g = 9.81      # m/s^2
m = 0.25      # kg
k = 0.1       # N·s/m
s0 = 300      # m
tol = 0.01    # precisión en segundos

def f(t):
    return s0 - (m * g / k) * t + (m**2 * g / k**2) * (1 - np.exp(-k * t / m))

def biseccion(a, b, tol):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo dado")
    iteraciones = []
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        iteraciones.append((a, b, c, fc))
        if fc == 0:
            return c, iteraciones
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, iteraciones

a = 0
b = 20

raiz, pasos = biseccion(a, b, tol)

print(f"Tiempo aproximado que tarda en caer el objeto: {raiz:.4f} segundos\n")
print("Iteraciones:")
print("N |     a     |     b     |     c     |     f(c)")
for i, (a_i, b_i, c_i, fc_i) in enumerate(pasos, 1):
    signo = ">" if fc_i > 0 else "<"
    print(f"{i:2d} | {a_i:8.4f} | {b_i:8.4f} | {c_i:8.4f} | {fc_i:10.4f} {signo} 0")
