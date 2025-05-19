import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-3, 3, 500)
y1 = x_vals**2 - 1
y2 = np.exp(1 - x_vals**2)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y1, label='y = x² - 1', color='blue')
plt.plot(x_vals, y2, label='y = e^{1 - x²}', color='green')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Gráficas de y = x² - 1 y y = e^{1 - x²}")
plt.grid(True)
plt.legend()

# Guardar imagen
plt.savefig("grafica_x2_vs_exp.png", dpi=300)
plt.close()
print(" Gráfica guardada como 'grafica_x2_vs_exp.png'")

def f(x):
    return x**2 - 1 - np.exp(1 - x**2)

def biseccion(a, b, tol=1e-3):
    pasos = []
    if f(a) * f(b) > 0:
        return None, pasos  # No hay cambio de signo
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        pasos.append((a, b, c))
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, pasos

raiz, iteraciones = biseccion(1, 2)

if raiz:
    print("\nMétodo de bisección para x² - 1 = e^{1 - x²}")
    print(f"Raíz aproximada: x ≈ {raiz:.3f}")
    print("Iteraciones:")
    for i, (a, b, c) in enumerate(iteraciones, 1):
        print(f"{i}: a={a:.6f}, b={b:.6f}, c={c:.6f}")
else:
    print(" No se encontró raíz en ese intervalo.")
