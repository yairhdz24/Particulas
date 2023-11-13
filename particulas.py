from PySide2.QtWidgets import QMessageBox
from particula import Particula
import json

class Particulas:
    def __init__(self):
        self.__particulas = []
        
    def __str__(self):
        return "".join(str(particulas) + "\n" for particulas in self.__particulas)
 
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self
        
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration    

    def agregar_final(self, particulas:Particula):
        self.__particulas.append(particulas)
        
    def agregar_inicio(self, particulas:Particula):
        self.__particulas.insert(0, particulas)
        
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
       
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=4)
                return 1
        except Exception as e:
            print("Error al guardar:", str(e))
            return 0  # Indica que hubo un error

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = []
    
                for datos_particula in lista:
                    id = datos_particula["id"]
                    origen_x = datos_particula["origen"]["x"]
                    origen_y = datos_particula["origen"]["y"]
                    destino_x = datos_particula["destino"]["x"]
                    destino_y = datos_particula["destino"]["y"]
                    red = datos_particula["color"]["red"]
                    green = datos_particula["color"]["green"]
                    blue = datos_particula["color"]["blue"]
                    velocidad = datos_particula["velocidad"]
    
                    particula = Particula(
                        id, origen_x, origen_y, destino_x, destino_y, red, green, blue, velocidad
                    )
    
                    self.__particulas.append(particula)
    
                return 1
        except Exception as e:
            print("Error al abrir:", str(e))
            return 0  # Indica que hubo un error


        
    #Ordena el id de manera acendente
    def ordenar_id(self):
        self.__particulas.sort(key=lambda particula: int(particula.id))


        #Ordena la distancia de manera descendiente
    def ordenar_distancia(self):
        self.__particulas = sorted(self.__particulas, key=lambda particula: particula.distancia, reverse=True)
            
    
    #Ordena la Velocidad de manera acsendente
    def ordenar_velocidad(self):
        self.__particulas = sorted(self.__particulas, key=lambda particula: particula.velocidad)



