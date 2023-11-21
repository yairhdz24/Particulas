import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, arista):
        origen = (arista['origen']['x'], arista['origen']['y'])
        destino = (arista['destino']['x'], arista['destino']['y'])
        distancia = arista['distancia']

        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, distancia))

        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[destino].append((origen, distancia))

    def obtener_vertices(self):
        return list(self.grafo.keys())

    def obtener_vecinos(self, vertice):
        return self.grafo[vertice]



#Algoritmo dijkstra
    def dijkstra(self, origen):
        distancias = {v: float('infinity') for v in self.obtener_vertices()}
        padres = {v: None for v in self.obtener_vertices()}
        distancias[origen] = 0

        heap = [(0, origen)]

        while heap:
            distancia_actual, vertice_actual = heapq.heappop(heap)

            if distancia_actual > distancias[vertice_actual]:
                continue

            for vecino, peso in self.obtener_vecinos(vertice_actual):
                distancia_nueva = distancias[vertice_actual] + peso

                if distancia_nueva < distancias[vecino]:
                    distancias[vecino] = distancia_nueva
                    padres[vecino] = vertice_actual
                    heapq.heappush(heap, (distancia_nueva, vecino))

        return distancias, padres

    