import heapq
from math import atan2
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
    
   # ALGORITMO PRIM
    def prim(self):
        vertices = self.obtener_vertices()

        if not vertices:
            return []
        
        visitados = set()  
        aristas = [] 
        vertice_inicial = vertices[0]  # tomar el primero
        visitados.add(vertice_inicial)

        # Inicializar heap con aristas conectadas al vértice inicial
        heap = [(peso, vertice_inicial, vecino) for vecino, peso in self.obtener_vecinos(vertice_inicial)]

        # conversion a cola
        heapq.heapify(heap)

        # Inicio del prim
        while heap:
            peso, vertice, vecino = heapq.heappop(heap)

            if vecino not in visitados:

                # vAISITADO
                visitados.add(vecino)

                # Agregar la arista al Arbol minimO
                aristas.append((vertice, vecino, peso))

                # Agregar las aristas conectadas al veciOO
                for vecino_vecino, peso_vecino in self.obtener_vecinos(vecino):
                    if vecino_vecino not in visitados:
                        heapq.heappush(heap, (peso_vecino, vecino, vecino_vecino))

        return aristas
    

    #Algoritmo Graham
    
    def graham_scan(self):

        def orientacion(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0 # debugging
            return 1 if val > 0 else 2  # En sentido horario o antihorario

        def comparador(punto):
            x, y = punto
            return atan2(y - punto_inicial[1], x - punto_inicial[0])

        # Obtener los puntos deesde el grafo
        puntos = self.obtener_vertices()

        if len(puntos) < 3:
            raise ValueError("Se necesitan al menos 3 puntos para formar un cierre convexo.")

        # Encontrar el punto con la coordenada y mas baja en caso de ser iguales se tomsa el izuierdo
        punto_inicial = min(puntos, key=lambda punto: (punto[1], punto[0]))

        # Ordenar los puntos segun el angulo polar depende el primer punto ( ni puta idea)
        puntos_ordenados = sorted(puntos, key=comparador)

        #  se guardan los dos primeros puntos
        pila = [punto_inicial, puntos_ordenados[0], puntos_ordenados[1]]

        for i in range(2, len(puntos)):
            while len(pila) > 1 and orientacion(pila[-2], pila[-1], puntos_ordenados[i]) != 2:
                pila.pop()
            pila.append(puntos_ordenados[i])

        return pila

    #Algoritmo kruskal
class GrafoKruskal:
    def __init__(self):
        self.aristas = []

    def agregar_arista(self, origen, destino, peso):
        self.aristas.append((origen, destino, peso))

    def obtener_vertices(self):
        vertices = set()
        for arista in self.aristas:
            vertices.add(arista[0])
            vertices.add(arista[1])
        return list(vertices)

    def kruskal(self):
        self.aristas.sort(key=lambda x: x[2])  # Ordenar aristas por peso

        conjuntos_disjuntos = {vertice: {vertice} for vertice in self.obtener_vertices()}
        arbol_minimo = []

        for arista in self.aristas:
            origen, destino, peso = arista

            conjunto_origen = conjuntos_disjuntos[origen]
            conjunto_destino = conjuntos_disjuntos[destino]

            if conjunto_origen != conjunto_destino:
                arbol_minimo.append(arista)

                # Unir conjuntos disjuntos
                conjunto_union = conjunto_origen.union(conjunto_destino)
                for vertice in conjunto_union:
                    conjuntos_disjuntos[vertice] = conjunto_union

        return arbol_minimo