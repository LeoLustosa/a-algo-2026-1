import time
import sys

# Aumenta o limite de recursões permitidas pelo Python para evitar o erro 'RecursionError' no n=1000
sys.setrecursionlimit(2000)

def fatorial(n):
    """
    Calcula o fatorial de um número utilizando recursão.
    """
    # Caso base: o fatorial de 0 é 1
    if n == 0:
        return 1
    # Chamada recursiva: n multiplicado pelo fatorial de (n-1)
    else:
        return n * fatorial(n-1)

def executar_testes_fatorial():
    """
    Mede o tempo de execução do algoritmo para diferentes valores de n.
    """
    valores_n = [10, 100, 500, 1000]
    
    print("Análise de Tempo de Execução - Fatorial Recursivo\n")
    print("-" * 50)
    
    for n in valores_n:
        inicio = time.time()
        resultado = fatorial(n)
        fim = time.time()
        
        tempo_execucao = fim - inicio
        
        print(f"Tempo para n = {n:<4}: {tempo_execucao:.8f} segundos")
    print("-" * 50)

if __name__ == "__main__":
    executar_testes_fatorial()