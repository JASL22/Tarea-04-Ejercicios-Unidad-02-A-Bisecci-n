def f(x):
    return x**3 - 7*x**2 + 14*x - 6

def biseccion(a, b, tol=1e-2):
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

intervalos = {
    "a": (0, 1),
    "b": (1, 3.2),
    "c": (3.2, 4)
}

for literal, (a, b) in intervalos.items():
    raiz, pasos = biseccion(a, b)
    if raiz is None:
        print(f"\nLiteral {literal.upper()}: No hay raíz en el intervalo [{a}, {b}]")
    else:
        print(f"\nLiteral {literal.upper()}: Raíz aproximada: x ≈ {round(raiz, 4)}")
        print("Iteraciones:")
        for i, (a_i, b_i, c_i) in enumerate(pasos, 1):
            print(f"{i}: a={a_i:.5f}, b={b_i:.5f}, c={c_i:.5f}")
