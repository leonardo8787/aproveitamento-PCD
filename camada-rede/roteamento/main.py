import heapq

def dijkstra(grafo, origem):
    distancias = {no: float('infinity') for no in grafo}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)
        if distancia_atual > distancias[no_atual]:
            continue
        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distancias = dijkstra(grafo, 'A')
print(distancias)
