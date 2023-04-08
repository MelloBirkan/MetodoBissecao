def bisseccao(f, a, b, epsilon, max_iter):
    if f(a) * f(b) >= 0:
        raise ValueError("A função f deve ter sinais opostos em a e b.")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 <= epsilon:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2



if __name__ == "__main__":
    # Função exemplo: f(x) = x^3 - x^2 - 2
    def f(x):
        return x**3 + 4*x**2 - 10

    a = 1
    b = 2
    epsilon = 1e-1

    raiz = bisseccao(f, a, b, epsilon, 3)
    print(f"A raiz aproximada de f no intervalo [{a}, {b}] com tolerância {epsilon} é {raiz}.")
