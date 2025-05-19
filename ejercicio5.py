import numpy as np

def f(x):
    return (x + 3) * (x + 1)**2 * x * (x - 1)**3 * (x - 3)

def biseccion(a, b, tol=1e-5):
    pasos = []
    if f(a) * f(b) > 0:
        return None, pasos 
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        pasos.append((a, b, c, f(c)))
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, pasos

# Intervalos a analizar
intervalos = [
    ("[-1.5, 2.5]", -1.5, 2.5),
    ("[-0.5, 2.4]", -0.5, 2.4),
    ("[-0.5, 3]", -0.5, 3),
    ("[-3, -0.5]", -3, -0.5)
]

for nombre, a, b in intervalos:
    raiz, pasos = biseccion(a, b)
    print(f"\n Intervalo {nombre}")
    if raiz:
        print(f"Raíz aproximada: x ≈ {raiz:.5f}")
        print(f"→ Converge al cero más cercano en el intervalo.")
    else:
        print(" No hay cambio de signo en este intervalo.")
