import time
import random


TAMANHOS_LISTA = [1000, 5000, 10000, 20000, 50000]


def insertion_sort(lista_desordenada):
    """
    Ordena uma lista em ordem crescente utilizando o algoritmo Insertion Sort.
    Complexidade de tempo no pior caso: O(n^2).
    """
    tamanho = len(lista_desordenada)
    
    for i in range(1, tamanho):
        chave = lista_desordenada[i]
        j = i - 1
        
        # Move os elementos da lista que são maiores que a chave
        # para uma posição à frente de sua posição atual
        while j >= 0 and lista_desordenada[j] > chave:
            lista_desordenada[j + 1] = lista_desordenada[j]
            j -= 1
            
        lista_desordenada[j + 1] = chave


def executar_testes():
    """
    Gera listas aleatórias, afere o tempo de execução do Insertion Sort e do Timsort (função nativa sorted),
    e imprime os resultados no terminal.
    """
    print("Iniciando a comparação de algoritmos...\n")
    print("-" * 60)
    
    for n in TAMANHOS_LISTA:
        # Gera uma lista aleatória de tamanho 'n'
        lista_original = [random.randint(1, 100000) for _ in range(n)]
        
        # Cópias para garantir que um algoritmo não ordene a lista do outro
        lista_para_insertion = lista_original.copy()
        lista_para_timsort = lista_original.copy()
        
        print(f"Testando para n = {n} elementos:")
        
        # 1. Teste do Insertion Sort
        inicio_insertion = time.time()
        insertion_sort(lista_para_insertion)
        fim_insertion = time.time()
        tempo_insertion = fim_insertion - inicio_insertion
        
        # 2. Teste da função nativa do Python (Timsort)
        inicio_timsort = time.time()
        lista_ordenada_nativa = sorted(lista_para_timsort)
        fim_timsort = time.time()
        tempo_timsort = fim_timsort - inicio_timsort
        
        # Resultados no terminal
        print(f"  -> Insertion Sort O(n^2):    {tempo_insertion:.5f} segundos")
        print(f"  -> Função sorted() O(n log n): {tempo_timsort:.5f} segundos")
        print("-" * 60)

# Executa o script
if __name__ == "__main__":
    executar_testes()