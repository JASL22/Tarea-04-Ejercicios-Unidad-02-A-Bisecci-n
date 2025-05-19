def f(x):
    return x**3 - x - 1

def biseccion(a, b, tol):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo dado")
    n_iter = 0
    while (b - a)/2 > tol:
        c = (a + b) / 2
        fc = f(c)
        n_iter += 1
        if fc == 0:
            return c, n_iter
        elif f(a) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, n_iter

a = 1
b = 2
tol = 1e-4

raiz, iteraciones = biseccion(a, b, tol)

print(f"Número de iteraciones necesarias (cota mínima): 14")
print(f"Número de iteraciones realizadas: {iteraciones}")
print(f"Aproximación de la raíz: {raiz:.6f}")
print(f"f(raiz) = {f(raiz):.6f}")
