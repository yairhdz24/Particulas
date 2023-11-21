from random import randint
from math import *

def distancia_euclidiana(x_1, y_1, x_2, y_2, decimales=5):
    distancia = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return round(distancia, decimales)


def distancia_entre_puntos(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return abs(x2 - x1) + abs(y2 - y1)

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
        min_distancia = float('infinity')
        punto_cercano = None
        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclidiana(x1, y1, x2, y2)
                if d < min_distancia:
                    min_distancia = d
                    punto_cercano = punto_j
        resultado.append((punto_i, punto_cercano))
    return resultado
