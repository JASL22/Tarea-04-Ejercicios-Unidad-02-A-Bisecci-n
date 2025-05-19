import numpy as np
import matplotlib.pyplot as plt

# Configuración de la gráfica
x_vals = np.linspace(-1.4, 1.4, 1000)
y1 = x_vals
y2 = np.tan(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y1, label='y = x', color='blue')
plt.plot(x_vals, y2, label='y = tan(x)', color='orange')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-10, 10)
plt.title("Gráficas de y = x y y = tan(x)")
plt.grid(True)
plt.legend()

# Guardar la imagen
plt.savefig("grafica_tanx_vs_x.png", dpi=300)
plt.close()
print("Gráfica guardada como 'grafica_tanx_vs_x.png'")

# Función y método de bisección
def f(x):
    return x - np.tan(x)

def biseccion(a, b, tol=1e-5, max_iter=100):
    iteraciones = []
    if f(a) * f(b) > 0:
        return None, []  # No hay cambio de signo
    
    for _ in range(max_iter):
        c = (a + b) / 2
        iteraciones.append((a, b, c, f(c)))
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iteraciones

# Aplicar bisección en un intervalo seguro (evitando π/2 ≈ 1.57)
raiz, pasos = biseccion(4.4, 4.7)

if raiz is not None:
    print("\nMétodo de bisección para x = tan(x)")
    print(f"Raíz aproximada: x ≈ {raiz:.5f}")
    print("Iteraciones:")
    print("{:<5} {:<12} {:<12} {:<12} {:<12}".format("Iter", "a", "b", "c", "f(c)"))
    for i, (a, b, c, fc) in enumerate(pasos, 1):
        print(f"{i:<5} {a:.7f} {b:.7f} {c:.7f} {fc:.7f}")
else:
    print("No se encontró raíz en ese intervalo. Verifica el cambio de signo.")