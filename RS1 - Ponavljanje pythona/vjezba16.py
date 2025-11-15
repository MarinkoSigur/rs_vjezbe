import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        trenutna_udaljenost, node = heapq.heappop(heap)

        if trenutna_udaljenost > distances[node]:
            continue

        for susjed, tezina in graph[node]:
            nova_udaljenost = trenutna_udaljenost + tezina

            if nova_udaljenost < distances[susjed]:
                distances[susjed] = nova_udaljenost
                heapq.heappush(heap, (nova_udaljenost, susjed))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))