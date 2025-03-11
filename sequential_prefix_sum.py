def soma_prefixos_sequencial(lista):
    soma_prefixos = [0] * len(lista)
    soma_acumulada = 0
    for i, num in enumerate(lista):
        soma_acumulada += num
        soma_prefixos[i] = soma_acumulada
    return soma_prefixos

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
print(soma_prefixos_sequencial(lista))
