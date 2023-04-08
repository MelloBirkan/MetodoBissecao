from math import cos
# Define a função bisseccao que implementa o método da bisseção
def bisseccao(f, a, b, epsilon, max_iter):
    # Verifica se os sinais da função nos limites do intervalo são opostos
    if f(a) * f(b) >= 0:
        return("A função f deve ter sinais opostos em a e b.")
    
    # Itera até atingir o número máximo de iterações
    for _ in range(max_iter):
        # Calcula o ponto médio do intervalo atual
        c = (a + b) / 2

        # Verifica se a função no ponto médio é zero ou se a tolerância foi atingida
        if f(c) == 0 or (b - a) / 2 <= epsilon:
            # Se sim, interrompe o loop e retorna o resultado
            break
        # Se a função em a e a função em c têm sinais opostos, atualiza o limite superior do intervalo
        elif f(a) * f(c) < 0:
            b = c
        # Caso contrário, atualiza o limite inferior do intervalo
        else:
            a = c

    # Retorna a melhor aproximação da raiz encontrada até o momento
    return (a + b) / 2

def aplicarBisseccao(f, a, b, epsilon, max_iter):
  # Chama a função bisseccao para encontrar uma aproximação da raiz de f no intervalo dado
    raiz = bisseccao(f, a, b, epsilon, max_iter)
    # Imprime a raiz aproximada encontrada
    print(f"A raiz aproximada de f no intervalo [{a}, {b}] com tolerância {epsilon} é {raiz}.")
  

if __name__ == "__main__":
# Exercicio 2(
    def f(x):
        return x**3 + 4*x**2 - 10

    a = 1
    b = 2
    epsilon = 1e-1
    aplicarBisseccao(f, a, b, epsilon, 3)
#)

# Exercicio 3(
    def A(x):
        return x - 2**(-x) 

    a = 0
    b = 1
    epsilon = 1e-2
    print("\nA)")
    aplicarBisseccao(A, a, b, epsilon, 3)



    def B(x):
        return 2.71828**3 - x**2 + (3*x) -2

    a = 0
    b = 1
    epsilon = 1e-2
    print("\nB) ")
    aplicarBisseccao(B, a, b, epsilon, 6)
  

    def C(x):
        return 2*x*cos(2*x) - (x-1)**2 

    intervalos = [(-3, -2), (-1, 0)]
    epsilon = 1e-3
    print("\nC) ")
    for i, (a, b) in enumerate(intervalos):
      try:
        aplicarBisseccao(C, a, b, epsilon, 6)
      except ValueError as e:
        print(f"Não foi possível encontrar uma raiz no intervalo [{a}, {b}]. Motivo: {e}")


    def D(x):
        return x*cos*x - 2*x**2 + 3*x - 1

    intervalos = [(-3, -2), (-1, 0)]
    epsilon = 1e-3
    print("\nD) ")
    for i, (a, b) in enumerate(intervalos):
      try:
        aplicarBisseccao(D, a, b, epsilon, 6)
      except ValueError as e:
        print(f"Não foi possível encontrar uma raiz no intervalo [{a}, {b}]. Motivo: {e}")
#)  