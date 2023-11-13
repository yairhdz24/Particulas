from random import randint
from math import *



def distancia_euclidiana(x_1, y_1, x_2, y_2, decimales=5):
    distancia = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return round(distancia, decimales)

# Puntos random
def Puntos_Random(n:int) -> list:
    puntos = []

    for i in range(n):
        x = randint(0, 500)  #no hagas caso a esto xd
        y = randint(0, 500)
        punto = (x, y)
        puntos.append(punto)
    return puntos

def Fuerza_Bruta(puntos_list)->list:
    resultado = []
    for punto_i in puntos_list:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 10000
        cercano = 10000
        cercano = (0, 0)
        for puntos_j in puntos_list:
            if punto_i != puntos_j:
                x2 = puntos_j[0]
                y2 = puntos_j[1]
                d = distancia_euclidiana(x1, y1, x2, y2)
                if d < min:
                    min = d
                    cercano = (x2, y2)
        resultado.append((punto_i, cercano))
    return resultado




# def crear_grafo(particulas):
#     grafo = {}  # Diccionario que representa el grafo

#     for particula in particulas:
#         origen = (particula.origen_x, particula.origen_y)
#         destino = (particula.destino_x, particula.destino_y)
#         distancia = distancia_euclidiana(origen[0], origen[1], destino[0], destino[1])

#         # Agregar arista desde origen a destino
#         if origen not in grafo:
#             grafo[origen] = []
#         grafo[origen].append((destino, distancia))

#         # Agregar arista desde destino a origen
#         if destino not in grafo:
#             grafo[destino] = []
#         grafo[destino].append((origen, distancia))

    return grafo



