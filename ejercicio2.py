import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Parte 1: Graficar y = x y y = sin(x) y guardar imagen
# --------------------------

x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y1 = x_vals
y2 = np.sin(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y1, label='y = x', color='blue')
plt.plot(x_vals, y2, label='y = sin(x)', color='green')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Gráficas de y = x y y = sin(x)")
plt.grid(True)

# Guardar la imagen
plt.savefig("grafica_funciones.png", dpi=300)
plt.close()  # Cierra la figura para evitar mostrarla si no es necesario

print("✅ Gráfica guardada como 'grafica_funciones.png'")

# --------------------------
# Parte 2: Método de bisección para x = 2 sin(x)
# --------------------------

def f(x):
    return x - 2 * np.sin(x)

def biseccion(a, b, tol=1e-5):
    iteraciones = []
    if f(a) * f(b) > 0:
        return None, []  # No hay cambio de signo
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        iteraciones.append((a, b, c))
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iteraciones

# Buscar raíz entre 1 y 2
raiz, pasos = biseccion(1, 2)

print("\nMétodo de bisección para x = 2 sin(x)")
print(f"Raíz aproximada: x ≈ {raiz:.5f}")
print("Iteraciones:")
for i, (a, b, c) in enumerate(pasos, 1):
    print(f"{i}: a={a:.7f}, b={b:.7f}, c={c:.7f}")
