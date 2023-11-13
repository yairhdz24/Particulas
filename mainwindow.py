from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QLabel, QGraphicsView, QGraphicsTextItem
from PySide2.QtCore import Slot
from PySide2 import QtCore
from PySide2.QtGui import QFont, QPen, QColor, QTransform, QWheelEvent, QPainter, QBrush
from random import randint
from pprint import pprint

from ui_mainwindow import Ui_MainWindow
from particula import Particula
from particulas import Particulas
from algoritmos import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.cargados_desde_json = False

        self.particulas = Particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1060, 600)
        # self.setWindowIcon(QtGui.QIcon("icono.png"))
        # self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))


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
        self.ui.salida.clear() #salida es el name del text edit


        if self.particulas:
            self.ui.salida.insertPlainText(f"\tGRAFO\n")
            print("\n\t\tGRAFO\n")

            for particula in self.particulas:
                grafo = particula.grafo()
                self.ui.salida.insertPlainText(f"{grafo}\n")
                pprint(grafo)
        else:
            QMessageBox.warning(
            self,
            "Error", "Inserta al menos una particula antes de mostrar"
            )
    

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
            "Inserta al menos una particula antes de ordenar."
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


            self.sceneAlgoritmos.addEllipse(origenX, origenY, 3, 3, pen, brush)
            #punto de destino
            self.sceneAlgoritmos.addEllipse(destinoX, destinoY, 3, 3, pen, brush)

   
    
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

    @Slot()
    def crear_grafo(self):
        grafo = {}  # Diccionario que representa el grafo

        for particula in self.particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            distancia = distancia_euclidiana(origen[0], origen[1], destino[0], destino[1])

            # Agregar arista desde origen a destino
            if origen not in grafo:
                grafo[origen] = []
            grafo[origen].append((destino, distancia))

            # Agregar arista desde destino a origen
            if destino not in grafo:
                grafo[destino] = []
            grafo[destino].append((origen, distancia))

            print(grafo)
        return grafo