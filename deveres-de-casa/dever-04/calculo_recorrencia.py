import math

def calcular_recorrencia(n):
    """
    Calcula recursivamente a funcao F(n) = 2F(n-1) + n^2.
    """
    # Caso base
    if n == 1:
        return 2
    
    # Passo recursivo usando math.pow para o n ao quadrado
    return 2 * calcular_recorrencia(n - 1) + int(math.pow(n, 2))


if __name__ == "__main__":
    print("--- Cálculo de Recorrência ---")
    print("Aviso: Algoritmo exponencial O(2^n). Evite valores muito altos.\n")
    
    try:
        valor_n = int(input("Digite o valor de n: "))
        
        if valor_n < 1:
            print("O valor precisa ser maior ou igual a 1.")
        else:
            resultado = calcular_recorrencia(valor_n)
            print(f"O resultado de F({valor_n}) é: {resultado}")
            
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")