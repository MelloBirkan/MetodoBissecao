def bisseccao(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        raise ValueError("A função f deve ter sinais opostos em a e b.")

    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# Exemplo de uso:
if __name__ == "__main__":
    # Função exemplo: f(x) = x^3 - x^2 - 2
    def f(x):
        return x**3 - x**2 - 2

    a = 1
    b = 2
    epsilon = 1e-6

    raiz = bisseccao(f, a, b, epsilon)
    print(f"A raiz aproximada de f no intervalo [{a}, {b}] com tolerância {epsilon} é {raiz}.")
