from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QLabel, QGraphicsView, QGraphicsTextItem, QGraphicsLineItem
from PySide2.QtCore import Slot
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import QFont, QPen, QColor, QTransform, QWheelEvent, QPainter, QBrush
from random import randint
from pprint import pprint
import random
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from particulas import Particulas
from algoritmos import *
from grafo import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.grafo = Grafo()

        self.cargados_desde_json = False

        self.particulas = Particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1060, 600)
        self.setWindowIcon(QtGui.QIcon("react.png"))
        self.setWindowTitle("Particulas")


        self.ui.pushButton_Agregar_Inicio.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_Agregar_Final.clicked.connect(self.click_agregar_final)
        self.ui.pushButton_Mostrar.clicked.connect(self.click_mostrar)
        self.ui.pushButton_Mostrar_Grafo.clicked.connect(self.click_mostrar_grafo)

        self.ui.pushButton_Ordenar_id.clicked.connect(self.click_ordenar_id)
        self.ui.pushButton_Ordenar_velocidad.clicked.connect(self.click_ordenar_velocidad)
        self.ui.pushButton_Ordenar_distancia.clicked.connect(self.click_ordenar_distancia)

        #para acceder al menu de los archivos
        self.ui.actionAbrir_archivo.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar_archivo.triggered.connect(self.action_Guardar_Archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        #funciones para dibujar particulas
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        self.ui.limpiar_pushButton_2.clicked.connect(self.limpiar)

        #Algotritmos
        self.ui.Mostrar_puntos_pushButton.clicked.connect(self.dibujar_puntos)
        self.ui.pushButton_dibujar_random.clicked.connect(self.dibujar_puntos_Random)
        self.ui.pushButton_Fuerza_bruta.clicked.connect(self.Fuerza_bruta)
        self.ui.pushButton_Dijkstra.clicked.connect(self.Dijkstra)
        self.ui.pushButton_Kruskal.clicked.connect(self.Kruskal)
        self.ui.pushButton_Prim.clicked.connect(self.Prim)
        self.ui.pushButton_Graham.clicked.connect(self.Graham)





        self.ui.spinBox_puntos.valueChanged.connect(self.spinBox_puntos)
        self.ui.horizontalSlider_2.valueChanged.connect(self.slider_puntos)


        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
        self.sceneAlgoritmos = QGraphicsScene()
        self.ui.graphicsView_Algoritmos.setScene(self.sceneAlgoritmos)
        # self.ui.graphicsView.scale(1.9, 0.9)

        # antialiasing que le quita lo pixeleado a las formas
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.ui.graphicsView_Algoritmos.setRenderHint(QPainter.Antialiasing)
        
        #Para que se pueda desplazar en la interfaz
        self.ui.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag) 
        self.ui.graphicsView_Algoritmos.setDragMode(QGraphicsView.ScrollHandDrag) 



        #para que el cursor cambie al acercarlo a un boton
        self.ui.pushButton_Agregar_Inicio.setCursor(QtCore.Qt.PointingHandCursor)
        self.ui.pushButton_Agregar_Final.setCursor(QtCore.Qt.PointingHandCursor)
        self.ui.pushButton_Mostrar.setCursor(QtCore.Qt.PointingHandCursor)
        self.ui.menuArchivo.setCursor(QtCore.Qt.PointingHandCursor)
        self.ui.menubar.setCursor(QtCore.Qt.PointingHandCursor)

    @Slot()
    def click_agregar_inicio(self):
        if self.validar_y_agregar_particula():
            self.particulas.agregar_inicio(self.crear_particula())
            self.actualizar_contador()

    @Slot()
    def click_agregar_final(self):
        if self.validar_y_agregar_particula():
            self.particulas.agregar_final(self.crear_particula())
            self.actualizar_contador()

    def validar_y_agregar_particula(self):
        id = self.ui.id_lineEdit.text()
        if self.particula_existente(id):
            return False

        if not self.validar_campos():
            return False

        return True

    def validar_campos(self):
        campos = [
            self.ui.id_lineEdit.text(),
            self.ui.origen_x_spinBox.value(),
            self.ui.origen_y_spinBox.value(),
            self.ui.destino_x_spinBox.value(),
            self.ui.destino_y_spinBox.value(),
            self.ui.velocidad_spinBox.value(),
        ]

        if any(not campo or campo == 0 for campo in campos):
            QMessageBox.warning(
                self,
                "Error",
                "Por favor, completa todos los campos antes de insertar una particula"
            )
            return False
        return True

    def crear_particula(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        return Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

    def particula_existente(self, id):
        for particula in self.particulas:
            if particula.id == id:
                QMessageBox.warning(self, "Error", "Ya existe una particula con ese ID. Ingresa otro ID único.")
                return True
        return False

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear() #salida es el name del text edit

        #verifica si existe una particula en la lista
        if self.particulas:
           self.ui.salida.insertPlainText(str(self.particulas))
        else:
          QMessageBox.warning(
            self,
            "Error", "Inserta al menos una particula antes de mostrar"
            )

    @Slot()
    def click_mostrar_grafo(self):
        self.ui.salida.clear()

        if self.particulas:
            self.ui.salida.insertPlainText("\tGRAFO\n")

            grafo = self.crear_grafo()
            print("\tGRAFO\n")
            pprint(grafo.grafo)

            for vertice, aristas in grafo.grafo.items():
                self.ui.salida.insertPlainText(f"Vertice: {vertice}\n")

                for arista in aristas:
                    destino, distancia = arista
                    self.ui.salida.insertPlainText(f"  -> {destino} (Distancia: {distancia})\n")

                self.ui.salida.insertPlainText("\n")

        else:
            QMessageBox.warning(
                self,
                "Error", "Inserta al menos una particula antes de mostrar"
            )

    @Slot()
    def imprimir_grafo(self, grafo):
        for origen, aristas in grafo.grafo.items():
            self.ui.salida.insertPlainText(f"Vértice: {origen}\n")
            for destino, distancia in aristas:
                self.ui.salida.insertPlainText(f"  -> {destino} (Distancia: {distancia})\n")

    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
             self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo correctamenet :D")
            self.cargados_desde_json = True  # se pone true para indicar que se cargo con json
            self.click_mostrar() #muestra automaticamente ;)
            self.mostrar_tabla()

            # grafo = crear_grafo_particulas(self.particulas.get_all_data())

            # Imprime el grafo (puedes ajustar cómo lo muestras)
          

        else:
            QMessageBox.warning(
                self,
                "Error",
                "No se pudo abrir el archivo ;( ")

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
             self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
        self,
        "Exito",
       "Archivo Guardado exitosamente :D" )
        else:
            QMessageBox.warning(
        self,
        "Error",
        "No se pudo guardar el archivo :C" )

    #Funciones para crear la tabla y la de busqueda

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10) #10 porque sonn 10 atributos con la distancia
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino y",
                   "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        font = QFont()
        font.setBold(True)  # Hace que el texto sea en negrita
        self.ui.tabla.horizontalHeader().setFont(font)

        # Estilo de los headers para la tabkla
        style = "QHeaderView::section { background-color: #DDDDDD;}"
        self.ui.tabla.horizontalHeader().setStyleSheet(style)


        self.ui.tabla.setRowCount(len(self.particulas))#crea columnas dependiendo las particulas que haya

        row = 0

        for particula in self.particulas:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))


            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        # Verificar si no hay particulas
        if not self.particulas:
            QMessageBox.warning(
                self,
                "Error",
                "Inserta al menos una particula antes de buscar."
            )
            return

        encontrado = False
        for particula in self.particulas:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10) #10 porque sonn 10 atributos con la distancia
                headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino y",
                           "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)

                font = QFont()
                font.setBold(True)  # Hace que el texto sea en negrita
                self.ui.tabla.horizontalHeader().setFont(font)

                # Estilo de los haders para la tabla
                style = "QHeaderView::section { background-color: #DDDDDD; }"
                self.ui.tabla.horizontalHeader().setStyleSheet(style)

                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))


                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                QMessageBox.information(
                    self,
                    "Exito",
                    f'Se encontro correctamente la Particula {id}')
                break

        if not encontrado:
            QMessageBox.warning(
                self,
                "Error",
                f"La particula con el ID: {id} no fue encontrada"
            )

    #Funciones de lIMPIAR Y DIBUJAR

    def wheelEvent(self, event: QWheelEvent) -> None:
    # ...
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
        
        if event.delta() > 0:
            self.ui.graphicsView_Algoritmos.scale(1.2, 1.2)
        else:
            self.ui.graphicsView_Algoritmos.scale(0.8, 0.8)

    # Luego, ajusta la vista para que las partículas sean visibles
        # self.ui.graphicsView.setSceneRect(self.scene.itemsBoundingRect())

    @Slot()
    def dibujar(self) -> None:
        pen = QPen()
        pen.setWidth(4) #Ancho de la linea

        escala = 2

         # Ordena las particulas por el atributo distancia
        #particulas_ordenadas = sorted(self.particulas, key=lambda particula: particula.distancia)

        for particula in self.particulas: #numero de particulas generadas

            red = particula.red   #se traen los valores de los colores
            green = particula.green
            blue = particula.blue

            color = QColor(red, green, blue)
            pen.setColor(color)

            x_origen = particula.origen_x   * escala #Valores insertados del origen y destino
            y_origen = particula.origen_y * escala
            x_destino = particula.destino_x * escala
            y_destino = particula.destino_y * escala

            self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)
            self.scene.addEllipse(x_destino, y_destino, 6, 6, pen)
            self.scene.addLine(x_origen + 3, y_origen + 3, x_destino + 3, y_destino + 3, pen)

            self.actualizar_contador()

    @Slot()
    def limpiar(self) -> None:
        print("limpio")
        self.scene.clear()
        self.sceneAlgoritmos.clear()

    @Slot()
    def actualizar_contador(self):
        cantidad_particulas = len(self.particulas)# se saca la cantidad de particulas
        #print(f"Contador de particulas: {cantidad_particulas}")
        self.ui.Contador_label.setText(f"Contador de particulas: {cantidad_particulas}")

    @Slot()
    def msg_error(self):
        QMessageBox.warning(
            self,
            "Error",
            "Inserta al menos una particula ."
        )
    
    # Ordenamiento de las particulas

    @Slot()
    def click_ordenar_id(self):
        if not self.particulas:
            self.msg_error()
        else:
            self.particulas.ordenar_id()
            self.click_mostrar()
            QMessageBox.information(self, "Éxito", "Se ordenaron las partículas por ID")

    @Slot()
    def click_ordenar_distancia(self):
        if not self.particulas:
            self.msg_error()
        else:
            self.particulas.ordenar_distancia()
            self.click_mostrar()
            QMessageBox.information(self, "Éxito", "Se ordenaron las partículas por distancia")

    @Slot()
    def click_ordenar_velocidad(self):
        if not self.particulas:
            self.msg_error()
        else:
            self.particulas.ordenar_velocidad()
            self.click_mostrar()
            QMessageBox.information(self, "Éxito", "Se ordenaron las partículas por velocidad")

    # extra- randoms y slider:
    @Slot(int)
    def spinBox_puntos(self, x):
        self.ui.horizontalSlider_2.setValue(x)

    @Slot(int)
    def slider_puntos(self, x):
        self.ui.spinBox_puntos.setValue(x)

    @Slot()
    def dibujar_puntos_Random(self):
        self.cargados_desde_json = False
        pen = QPen()
        pen.setWidth(3)
        brush = QBrush(QColor(0, 0, 0)) 
            
        self.puntos = Puntos_Random(self.ui.spinBox_puntos.value())
        # print(self.puntos)

        for punto in self.puntos:
            x = punto[0]
            y = punto[1]
            self.sceneAlgoritmos.addEllipse(x, y, 3, 3, pen, brush)

    # Algoritmos--

    @Slot()
    def obtener_puntos(self):
        puntos = []
        for particula in self.particulas:
            punto_origen = (particula.origen_x, particula.origen_y)
            punto_destino = (particula.destino_x, particula.destino_y)
            puntos.append(punto_origen)
            puntos.append(punto_destino)
        return puntos


    @Slot()
    def dibujar_puntos(self):
        self.cargados_desde_json = True
        self.scene.clear()

        pen = QPen()
        pen.setWidth(3)

        self.puntos = self.obtener_puntos()

        for particula in self.particulas:
            origenX = int(particula.origen_x)
            origenY = int(particula.origen_y)
            destinoX = int(particula.destino_x)
            destinoY = int(particula.destino_y)
            # red = int(particula.red)
            # green = int(particula.green)
            # blue = int(particula.blue)

           
            color = QColor(0, 0, 0)
            pen.setColor(color)
            brush = QBrush(QColor(color))


            self.sceneAlgoritmos.addEllipse(origenX, origenY, 2, 2, pen, brush)
            #punto de destino
            self.sceneAlgoritmos.addEllipse(destinoX, destinoY, 2, 2, pen, brush)

   
    
    @Slot()
    def Fuerza_bruta(self):
        resultado = Fuerza_Bruta(self.puntos)
        
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 0))  # Color de la linea roja

        print("Puntos Cercanos:")
        labels_added = set()  # Para mantener un registro de las etiquetas que se crean xd

        for i, (punto1, punto2) in enumerate(resultado, start=1):
            x1, y1 = punto1[0], punto1[1]
            x2, y2 = punto2[0], punto2[1]

            print(f"({x1}, {y1}) --> ({x2}, {y2})")

            # pone las lineeas con +2 de pading
            self.sceneAlgoritmos.addLine(x1 + 2, y1 + 2, x2 + 2, y2 + 2, pen)
            

            if self.cargados_desde_json:  # mita si los puntos se cargaron desde  un .json
                
                label1 = QGraphicsTextItem(f"{i} ({x1}),({y1})") # coordenadas de los puntos
                # label2 = QGraphicsTextItem(f"Punto {i + 1}")

                if label1 not in labels_added: # para que no se creen labels repetidos con el mismo id
                    label1.setPos(x1 + 5, y1 - 10)
                    font = QFont()
                    font.setPixelSize(5)  # tamano del label 7
                    label1.setFont(font) 
                    self.sceneAlgoritmos.addItem(label1)
                    labels_added.add(label1)
                    self.dibujar_puntos() # para que los puntos queden sobre lka linea

   
    @Slot()  # Crea el grafo son las prticulas cargadas y se manda a llmar en mostrar grafo
    def crear_grafo(self):
        grafo = Grafo()
    
        for particula in self.particulas:
            origen = {'x': particula.origen_x, 'y': particula.origen_y}
            destino = {'x': particula.destino_x, 'y': particula.destino_y}
            distancia = particula.distancia
    
            grafo.agregar_arista({
                'origen': origen,
                'destino': destino,
                'distancia': distancia
            })
    
        return grafo

    @Slot()  # Algoritmo dijkstra
    def Dijkstra(self):
        if not self.particulas:
            self.msg_error()
            return

        grafo = self.crear_grafo()
        vertices = grafo.obtener_vertices()

        # Dibujar el grafo original en la escena
        self.dibujar()

        origen = vertices[0]  # Puedes elegir cualquier vertice como origen, aqui tome el primero.
        # destino = random.choice(vertices)  # Elegir un vertice aleatorio como destino
        destino = vertices[1]  # Elegir un vertice aleatorio como destino

        distancias, padres = grafo.dijkstra(origen)

        # Reconstruir el camino desde el destino hasta el origen
        camino = [destino]
        while padres[camino[-1]] is not None:
            camino.append(padres[camino[-1]])
        camino.reverse()
        
        pprint(f"camino mas corto {camino}")

        # Dibujar el camino mas corto en la escena
        pen_camino = QPen()
        pen_camino.setWidth(2)
        pen_camino.setColor(QColor(0, 255, 0))  # Color del camino (puedes ajustar esto)
        

        for i in range(len(camino) - 1):
            punto_actual = camino[i]
            punto_siguiente = camino[i + 1]

            x_actual, y_actual = punto_actual
            x_siguiente, y_siguiente = punto_siguiente

            self.sceneAlgoritmos.addLine(x_actual + 2, y_actual + 2, x_siguiente + 2, y_siguiente + 2, pen_camino)
            self.dibujar_puntos()

        # Dibujar el grafo original y el destino
        pen_original = QPen()
        pen_original.setColor(QColor(0, 0, 0))
        pen_original.setWidth(3)


        # for particula in self.particulas:
        #     x_origen = particula.origen_x
        #     y_origen = particula.origen_y
        #     x_destino = particula.destino_x
        #     y_destino = particula.destino_y

        #     self.sceneAlgoritmos.addEllipse(x_origen + 4 , y_origen, 3, 3,  pen_original, brush)
        #     self.sceneAlgoritmos.addEllipse(x_destino, y_destino, 3, 3,  pen_original, brush)
        #     self.sceneAlgoritmos.addLine(x_origen + 4, y_origen + 4, x_destino + 4, y_destino + 4, pen_original)


    @Slot()  # Algoritmo de Kruskal
    def Kruskal(self):
        if not self.particulas:
            self.msg_error()
            return

        # Crear e inicializar el grafo para Kruskal
        grafo_kruskal = GrafoKruskal()
        for particula in self.particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            peso = particula.velocidad
            grafo_kruskal.agregar_arista(origen, destino, peso)

        # Obtener el árbol mínimo de Kruskal
        arbol_minimo = grafo_kruskal.kruskal()

        # Imprimir el árbol mInimo en la consola
        print("Arbol mInimo de Kruskal:", arbol_minimo)

        # Dibujar el árbol mínimo en la escena
        pen_arbol_minimo = QPen()
        pen_arbol_minimo.setWidth(2)
        pen_arbol_minimo.setColor(QColor(255, 0, 0))  # Color del árbol mínimo (puedes ajustar esto)

        for arista in arbol_minimo:
            origen, destino, peso = arista
            x_origen, y_origen = origen
            x_destino, y_destino = destino

            # Dibujar arista en la escena
            self.sceneAlgoritmos.addLine(x_origen, y_origen, x_destino, y_destino, pen_arbol_minimo)
            self.dibujar_puntos()
   

    @Slot()  # Algoritmo de Prim
    def Prim(self):
        if not self.particulas:
            self.msg_error()
            return

        grafo = self.crear_grafo()

        self.dibujar()

        # Ejecutar algoritmo de Prim
        arbol_minimo = grafo.prim()

        print(f"Arbol mInimo de Prim: {arbol_minimo}")
        
        # Dibujar el árbol mínimo en la escena

        
        pen_arbol_minimo = QPen()
        pen_arbol_minimo.setWidth(2)
        pen_arbol_minimo.setColor(QColor(255, 0, 0))  # Color del árbol mínimo (puedes ajustar esto)

        for arista in arbol_minimo:
            vertice, vecino, peso = arista
            x_vertice, y_vertice = vertice
            x_vecino, y_vecino = vecino

            # Dibujar arista en la escena
            self.sceneAlgoritmos.addLine(x_vertice, y_vertice, x_vecino, y_vecino, pen_arbol_minimo)
            self.dibujar_puntos()

            
    @Slot()
    def Graham(self):
        if not self.particulas:
            self.msg_error()
            return

        grafo = self.crear_grafo()
        

        # Ejecutar algoritmo de Graham
        convex_hull = grafo.graham_scan()

        print(f"Cierre convexo de Graham: {convex_hull}")

        # Dibujar el cierre convexo en la escena
        pen_convex_hull = QPen()
        pen_convex_hull.setWidth(2)
        pen_convex_hull.setColor(QColor(0, 0, 255))  # Color del cierre convexo 

        for i in range(len(convex_hull) - 1):
            vertice = convex_hull[i]
            vecino = convex_hull[i + 1]
            x_vertice, y_vertice = vertice
            x_vecino, y_vecino = vecino

            # Dibujar arista en la escena
            self.sceneAlgoritmos.addLine(x_vertice, y_vertice + 2 , x_vecino + 2, y_vecino + 2, pen_convex_hull)

        # Conectar el ultimo punto con el primero para cerrar el cierre convexo
        x_primer_punto, y_primer_punto = convex_hull[0]
        self.sceneAlgoritmos.addLine(x_vecino, y_vecino + 2, x_primer_punto + 2, y_primer_punto + 2, pen_convex_hull)
        self.dibujar_puntos()
