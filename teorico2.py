import numpy as np

def f(x):
    return np.sin(np.pi * x)

def biseccion(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo dado.")
    
    iteraciones = 0
    while (b - a)/2 > tol and iteraciones < max_iter:
        c = (a + b)/2
        fc = f(c)
        if abs(fc) < tol:
            return c, iteraciones
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    
    return (a + b)/2, iteraciones

casos = {
    "Caso 1 (a+b < 2)": (-0.5, 2.0),
    "Caso 2 (a+b = 2)": (-0.5, 2.5),
    "Caso 3 (a+b > 2)": (-0.5, 2.7)
}

print("Método de bisección para f(x) = sin(πx)")
print("="*50)

for nombre, (a, b) in casos.items():
    try:
        raiz, iteraciones = biseccion(f, a, b)
        print(f"{nombre}:")
        print(f" Intervalo = [{a}, {b}]")
        print(f" a + b = {a + b}")
        print(f" Raíz aproximada = {raiz:.6f}")
        print(f" f(raíz) = {f(raiz):.6e}")
        print(f" Iteraciones = {iteraciones}")
        print("-" * 50)
    except ValueError as e:
        print(f"{nombre}: Error - {str(e)}")
        print("-" * 50)