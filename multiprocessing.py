import multiprocessing

def calcular_prefixo(lista, inicio, fim, soma_inicial):
    soma_acumulada = soma_inicial
    prefixos = [0] * (fim - inicio)
    for i in range(inicio, fim):
        soma_acumulada += lista[i]
        prefixos[i - inicio] = soma_acumulada
    return prefixos

def soma_prefixos_paralela(lista, num_processos=4):
    tamanho = len(lista)
    blocos = [(i * tamanho // num_processos, (i + 1) * tamanho // num_processos) for i in range(num_processos)]
    somas_iniciais = [sum(lista[:inicio]) for inicio, _ in blocos]

    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = [pool.apply(calcular_prefixo, args=(lista, inicio, fim, soma_inicial))
                      for (inicio, fim), soma_inicial in zip(blocos, somas_iniciais)]

    soma_prefixos = []
    for r in resultados:
        soma_prefixos.extend(r)
    return soma_prefixos

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
print(soma_prefixos_paralela(lista))
