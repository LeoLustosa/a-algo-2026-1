def verifica_palindromo(arr):
    """
    Verifica se um array e palindromo usando recursao.
    """
    # Caso base: array vazio ou com 1 elemento
    if len(arr) <= 1:
        return True
    
    # Se as pontas forem diferentes, nao e palindromo
    if arr[0] != arr[-1]:
        return False
    
    # Chamada recursiva passando o array sem o primeiro e o ultimo elemento
    return verifica_palindromo(arr[1:-1])


if __name__ == "__main__":
    # Arrays de teste passados na aula
    array1 = [0, 1, 2, 3, 2, 1, 0]
    array2 = ["a", "b", "b", "a"]
    array3 = ["a", "b", "c", "b", "a"]
    array4 = ["a", "b", "c", "f", "b", "a"]

    print(f'array1 = {array1} -> {"É palíndromo" if verifica_palindromo(array1) else "Não é palíndromo"}')
    print(f'array2 = {array2} -> {"É palíndromo" if verifica_palindromo(array2) else "Não é palíndromo"}')
    print(f'array3 = {array3} -> {"É palíndromo" if verifica_palindromo(array3) else "Não é palíndromo"}')
    print(f'array4 = {array4} -> {"É palíndromo" if verifica_palindromo(array4) else "Não é palíndromo"}')