import numpy as np

L = 10     # cm
r = 1      # cm
V_obj = 12.4  # cm^3
tol = 0.01  # precisión

def f(h):
    if h < 0 or h > r:
        return np.nan
    return L * (0.5 * np.pi * r**2 - r**2 * np.arcsin(h / r) - h * np.sqrt(r**2 - h**2)) - V_obj

def biseccion(a, b, tol):
    iteraciones = []
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo dado")
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        iteraciones.append((a, b, c, fc))
        if fc == 0 or (b - a) / 2 < tol:
            break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return c, iteraciones

# Intervalo inicial
a = 0.0
b = 0.25

raiz, pasos = biseccion(a, b, tol)

print(f"Profundidad aproximada h ≈ {raiz:.5f} cm con error menor a {tol} cm\n")
print("Iteraciones:")
print("N |     a     |     b     |     c     |    f(c)")
for i, (a_i, b_i, c_i, fc_i) in enumerate(pasos, 1):
    signo = ">" if fc_i > 0 else "<"
    print(f"{i:2d} | {a_i:.5f} | {b_i:.5f} | {c_i:.5f} | {fc_i:.5f} {signo} 0")

print(f"\nResultado final: la profundidad del agua es aproximadamente h = {raiz:.5f} cm")
