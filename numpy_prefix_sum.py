import numpy as np

def soma_prefixos_numpy(lista):
    return np.cumsum(lista).tolist()

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
print(soma_prefixos_numpy(lista))
