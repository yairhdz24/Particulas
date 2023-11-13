from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, 
                 destino_x=0, destino_y=0, velocidad=0,
                 red=0, green=0, blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)

    def __str__(self):
        return (
            "id: " + str(self.__id) + "\n" +
            "Origen X: " + str(self.__origen_x) + "\n" +
            "Origen y: " + str(self.__origen_y) + "\n" +
            "Destino X: " + str(self.__destino_x) + "\n" +
            "Destino Y: " + str(self.__destino_y) + "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "Red: " + str(self.__red) + "\n" +
            "Green: " + str(self.__green) + "\n" +
            "Blue: " + str(self.__blue) + "\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )

    # def to_dict(self):
    #     return {
    #         "id": int(self.__id),
    #         "origen_x": self.__origen_x,
    #         "origen_y": self.__origen_y,
    #         "destino_x": self.__destino_x,
    #         "destino_y": self.__destino_y,
    #         "velocidad": self.__velocidad,
    #         "red": self.__red,
    #         "green": self.__green,
    #         "blue": self.__blue
    #     }

#Cambio del to_dict representar como grafo

    def to_dict(self):
      return {
          "id": self.__id,
          "origen": {
              "x": self.__origen_x,
              "y": self.__origen_y
          },
          "destino": {
              "x": self.__destino_x,
              "y": self.__destino_y
          },
          "color": {
              "red": self.__red,
              "green": self.__green,
              "blue": self.__blue
          },
          "velocidad": self.__velocidad
      }

    
    def grafo(self):
        return {
            "(" + str(self.__origen_x) + ", " + str(self.__origen_y) + "): [(" + str(self.__destino_x) + ", " + str(self.__destino_y) + "), " +  str(int(self.__distancia)) + "]"
        }

    @property
    def id(self):
        return self.__id

    @property
    def origen_x(self):
        return self.__origen_x

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x  

    @property
    def destino_y(self):
        return self.__destino_y
    
    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue
    
    @property
    def distancia(self):
        return self.__distancia


