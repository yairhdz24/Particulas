# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 545)
        MainWindow.setStyleSheet(u"/*FUENTE NAME: MS Shell Dlg 2*/\n"
"\n"
"/* Estilo para el t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
" \n"
"}\n"
"\n"
"/* Estilo para Bot\u00f3n (QPushButton) */\n"
"QPushButton {\n"
"    background-color: #1e6091; /* Azul oscuro para el fondo */\n"
"    color: white; /* Color del texto */\n"
"    border: 2px solid #1e6091; /* Borde con color */\n"
"    border-radius: 5px; /* Bordes redondeados */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Color de fondo en hover */\n"
"    border: 2px solid #2980b9; /* Borde en hover */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: #e4e4e4; /* Color de fondo */\n"
"    border: 1px solid #bdc3c7; /* Borde con color */\n"
"    border-radius: 3px; /* Bordes redondeados */\n"
"    padding: 2px; /* Espaciado interno */\n"
"    color: #333; /* Color del texto */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"                background: #0074D9;\n"
"                color: #FFFFFF;\n"
"            "
                        "    padding: 5px 10px;\n"
"                border: 1px solid #0056b3;\n"
"                border-top-left-radius: 5px;\n"
"                border-top-right-radius: 5px;\n"
"            }\n"
" \n"
"QTabBar::tab:selected {\n"
"                background: #0056b3;\n"
" }\n"
"\n"
"QMessageBox {\n"
"    background-color: #FFFFFF; /* Color de fondo */\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: #333333; /* Color del texto del mensaje */\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    background-color: #0074D9; /* Color del bot\u00f3n */\n"
"    color: #FFFFFF; /* Color del texto del bot\u00f3n */\n"
"    border: 1px solid #0056b3; /* Borde del bot\u00f3n */\n"
"    border-radius: 5px; /* Bordes redondeados */\n"
"    padding: 5px 10px; /* Espaciado interno del bot\u00f3n */\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"    background-color: #0056b3; /* Cambiar color de fondo al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #f0f0f0; /* Color de fondo azul claro */\n"
"    borde"
                        "r: 1px solid #808080; /* Borde gris de 2 p\u00edxeles */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QLabel{\n"
"	border: 0px\n"
"\n"
"}\n"
"\n"
"QLabel_21{\n"
"  color: blue;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #f0f0f0; \n"
"    border: 1px solid #ccc;\n"
"    height: 5px; \n"
"    border-radius: 2px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e6091;\n"
"    border: 1px solid #1e6091;\n"
"    width: 10px;\n"
"    margin: -8px 0; \n"
"    border-radius: 2px; /* Bordes redondeados para el manejador */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #ccc; /* Color del \u00e1rea izquierda del manejador */\n"
"    border: 1px solid #ccc; /* Borde de color claro */\n"
"    border-radius: 2px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #1e6091; /* Color del \u00e1rea derecha del manejador */\n"
"    border: 1px solid #1e6091; /* Borde de color azul */\n"
"    border-radius: 2p"
                        "x; /* Bordes redondeados */\n"
"}\n"
"\n"
"QGroupBox {\n"
" background-color: #FFFFFF;\n"
" border: 1px solid gray;\n"
" border-radius: 5px;\n"
"                      }\n"
"QLabel{\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.actionAbrir_archivo = QAction(MainWindow)
        self.actionAbrir_archivo.setObjectName(u"actionAbrir_archivo")
        font = QFont()
        font.setPointSize(10)
        self.actionAbrir_archivo.setFont(font)
        self.actionGuardar_archivo = QAction(MainWindow)
        self.actionGuardar_archivo.setObjectName(u"actionGuardar_archivo")
        self.actionGuardar_archivo.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_14 = QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.tabWidget.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_10 = QGridLayout(self.tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer = QSpacerItem(15, 562, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setStyleSheet(u"QGroupBox::title{\n"
"\n"
"subcontrol-position: top center;\n"
"}")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_11 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.groupBox_2)
        self.salida.setObjectName(u"salida")
        font3 = QFont()
        font3.setFamily(u"Poppins")
        self.salida.setFont(font3)

        self.gridLayout.addWidget(self.salida, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_11 = QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_8 = QSpacerItem(508, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_8, 0, 0, 1, 4)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox_4.setFont(font4)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        font5 = QFont()
        font5.setFamily(u"Poppins")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox_4)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        font6 = QFont()
        font6.setFamily(u"Poppins")
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.origen_y_spinBox.setFont(font6)
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.origen_y_spinBox, 1, 5, 1, 1)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setLineWidth(5)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(False)
        self.label_13.setIndent(-4)

        self.gridLayout_3.addWidget(self.label_13, 1, 4, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_17, 0, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox_4)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setFont(font6)
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.origen_x_spinBox, 1, 3, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_4, 3, 0, 1, 2)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font4)
        self.gridLayout_18 = QGridLayout(self.groupBox_7)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_16, 1, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox_7)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setFont(font6)
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_18.addWidget(self.destino_y_spinBox, 1, 4, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox_7)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setFont(font6)
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout_18.addWidget(self.destino_x_spinBox, 1, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_15, 1, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_7, 4, 0, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(238, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_5, 6, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font4)
        self.gridLayout_6 = QGridLayout(self.groupBox_10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_16 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.pushButton_Ordenar_id = QPushButton(self.groupBox_10)
        self.pushButton_Ordenar_id.setObjectName(u"pushButton_Ordenar_id")
        self.pushButton_Ordenar_id.setFont(font6)

        self.gridLayout_6.addWidget(self.pushButton_Ordenar_id, 1, 0, 1, 1)

        self.pushButton_Ordenar_distancia = QPushButton(self.groupBox_10)
        self.pushButton_Ordenar_distancia.setObjectName(u"pushButton_Ordenar_distancia")
        self.pushButton_Ordenar_distancia.setFont(font6)

        self.gridLayout_6.addWidget(self.pushButton_Ordenar_distancia, 2, 0, 1, 1)

        self.pushButton_Ordenar_velocidad = QPushButton(self.groupBox_10)
        self.pushButton_Ordenar_velocidad.setObjectName(u"pushButton_Ordenar_velocidad")
        self.pushButton_Ordenar_velocidad.setFont(font6)

        self.gridLayout_6.addWidget(self.pushButton_Ordenar_velocidad, 3, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_10, 7, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font4)
        self.verticalLayout = QVBoxLayout(self.groupBox_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_15 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_15)

        self.pushButton_Agregar_Inicio = QPushButton(self.groupBox_9)
        self.pushButton_Agregar_Inicio.setObjectName(u"pushButton_Agregar_Inicio")
        self.pushButton_Agregar_Inicio.setFont(font6)

        self.verticalLayout.addWidget(self.pushButton_Agregar_Inicio)

        self.pushButton_Agregar_Final = QPushButton(self.groupBox_9)
        self.pushButton_Agregar_Final.setObjectName(u"pushButton_Agregar_Final")
        self.pushButton_Agregar_Final.setFont(font6)

        self.verticalLayout.addWidget(self.pushButton_Agregar_Final)


        self.gridLayout_11.addWidget(self.groupBox_9, 7, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.groupBox)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font4)
        self.gridLayout_9 = QGridLayout(self.groupBox_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_18 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)

        self.pushButton_Mostrar = QPushButton(self.groupBox_11)
        self.pushButton_Mostrar.setObjectName(u"pushButton_Mostrar")
        self.pushButton_Mostrar.setFont(font6)

        self.gridLayout_9.addWidget(self.pushButton_Mostrar, 1, 0, 1, 1)

        self.pushButton_Mostrar_Grafo = QPushButton(self.groupBox_11)
        self.pushButton_Mostrar_Grafo.setObjectName(u"pushButton_Mostrar_Grafo")
        self.pushButton_Mostrar_Grafo.setFont(font6)

        self.gridLayout_9.addWidget(self.pushButton_Mostrar_Grafo, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_11, 7, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(17, 109, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 3, 2, 2, 1)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_14 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 0, 1, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox_6)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setFont(font6)
        self.blue_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.blue_spinBox, 2, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"color: green;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: blue;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_6)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setFont(font6)
        self.green_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.green_spinBox, 3, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_6)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setFont(font6)
        self.red_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.red_spinBox, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"color: red;")

        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_6, 3, 3, 2, 1)

        self.groupBox_8 = QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font4)
        self.gridLayout_19 = QGridLayout(self.groupBox_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.velocidad_spinBox = QSpinBox(self.groupBox_8)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        font7 = QFont()
        font7.setFamily(u"Poppins")
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setWeight(75)
        font7.setStrikeOut(False)
        self.velocidad_spinBox.setFont(font7)
        self.velocidad_spinBox.setMaximum(500)

        self.gridLayout_19.addWidget(self.velocidad_spinBox, 2, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_8, 5, 0, 1, 4)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font4)
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.id_lineEdit = QLineEdit(self.groupBox_5)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        font8 = QFont()
        font8.setFamily(u"Poppins")
        font8.setPointSize(8)
        self.id_lineEdit.setFont(font8)
        self.id_lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.id_lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color: #e4e4e4\n"
"}")
        self.id_lineEdit.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_8.addWidget(self.id_lineEdit, 1, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_5, 1, 0, 1, 4)


        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setFont(font8)

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setFont(font5)

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")
        self.mostrar_tabla_pushButton.setFont(font5)

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.limpiar_pushButton = QPushButton(self.tab_4)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")
        self.limpiar_pushButton.setFont(font5)

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 2, 1, 1, 1)

        self.dibujar_pushButton = QPushButton(self.tab_4)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")
        self.dibujar_pushButton.setFont(font5)

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 2, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setResizeAnchor(QGraphicsView.NoAnchor)

        self.gridLayout_5.addWidget(self.graphicsView, 1, 0, 1, 2)

        self.Contador_label = QLabel(self.tab_4)
        self.Contador_label.setObjectName(u"Contador_label")
        self.Contador_label.setFont(font8)

        self.gridLayout_5.addWidget(self.Contador_label, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_17 = QGridLayout(self.tab_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_16 = QGroupBox(self.tab_3)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setFont(font4)
        self.gridLayout_21 = QGridLayout(self.groupBox_16)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalSpacer_24 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_24, 0, 0, 1, 1)

        self.pushButton_Kruskal = QPushButton(self.groupBox_16)
        self.pushButton_Kruskal.setObjectName(u"pushButton_Kruskal")
        self.pushButton_Kruskal.setFont(font4)

        self.gridLayout_21.addWidget(self.pushButton_Kruskal, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_16, 0, 4, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_3)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setFont(font4)
        self.gridLayout_20 = QGridLayout(self.groupBox_15)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_23 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_23, 0, 0, 1, 1)

        self.pushButton_Dijkstra = QPushButton(self.groupBox_15)
        self.pushButton_Dijkstra.setObjectName(u"pushButton_Dijkstra")
        self.pushButton_Dijkstra.setFont(font4)

        self.gridLayout_20.addWidget(self.pushButton_Dijkstra, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_15, 0, 3, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab_3)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setFont(font4)
        self.gridLayout_12 = QGridLayout(self.groupBox_13)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_21 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_21, 0, 0, 1, 1)

        self.pushButton_Fuerza_bruta = QPushButton(self.groupBox_13)
        self.pushButton_Fuerza_bruta.setObjectName(u"pushButton_Fuerza_bruta")
        self.pushButton_Fuerza_bruta.setFont(font4)

        self.gridLayout_12.addWidget(self.pushButton_Fuerza_bruta, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_13, 0, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_3)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setFont(font4)
        self.gridLayout_13 = QGridLayout(self.groupBox_14)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_22 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_22, 0, 0, 1, 1)

        self.pushButton_Prim = QPushButton(self.groupBox_14)
        self.pushButton_Prim.setObjectName(u"pushButton_Prim")
        self.pushButton_Prim.setFont(font4)

        self.gridLayout_13.addWidget(self.pushButton_Prim, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_14, 0, 2, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_3)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font4)
        self.gridLayout_7 = QGridLayout(self.groupBox_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_19 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_19, 0, 0, 1, 1)

        self.Mostrar_puntos_pushButton = QPushButton(self.groupBox_12)
        self.Mostrar_puntos_pushButton.setObjectName(u"Mostrar_puntos_pushButton")
        self.Mostrar_puntos_pushButton.setFont(font4)

        self.gridLayout_7.addWidget(self.Mostrar_puntos_pushButton, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_12, 0, 0, 1, 1)

        self.spinBox_puntos = QSpinBox(self.tab_3)
        self.spinBox_puntos.setObjectName(u"spinBox_puntos")
        font9 = QFont()
        font9.setFamily(u"Poppins")
        font9.setPointSize(11)
        self.spinBox_puntos.setFont(font9)
        self.spinBox_puntos.setMinimum(2)
        self.spinBox_puntos.setMaximum(10000)

        self.gridLayout_17.addWidget(self.spinBox_puntos, 2, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.tab_3)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setFont(font4)
        self.gridLayout_22 = QGridLayout(self.groupBox_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_25 = QSpacerItem(88, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_25, 0, 0, 1, 1)

        self.pushButton_Graham = QPushButton(self.groupBox_17)
        self.pushButton_Graham.setObjectName(u"pushButton_Graham")
        self.pushButton_Graham.setFont(font4)

        self.gridLayout_22.addWidget(self.pushButton_Graham, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_17, 0, 5, 1, 1)

        self.graphicsView_Algoritmos = QGraphicsView(self.tab_3)
        self.graphicsView_Algoritmos.setObjectName(u"graphicsView_Algoritmos")

        self.gridLayout_17.addWidget(self.graphicsView_Algoritmos, 1, 0, 1, 6)

        self.limpiar_pushButton_2 = QPushButton(self.tab_3)
        self.limpiar_pushButton_2.setObjectName(u"limpiar_pushButton_2")
        self.limpiar_pushButton_2.setFont(font5)

        self.gridLayout_17.addWidget(self.limpiar_pushButton_2, 2, 5, 1, 1)

        self.pushButton_dibujar_random = QPushButton(self.tab_3)
        self.pushButton_dibujar_random.setObjectName(u"pushButton_dibujar_random")
        self.pushButton_dibujar_random.setFont(font5)

        self.gridLayout_17.addWidget(self.pushButton_dibujar_random, 2, 4, 1, 1)

        self.horizontalSlider_2 = QSlider(self.tab_3)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setFont(font3)
        self.horizontalSlider_2.setMinimum(2)
        self.horizontalSlider_2.setMaximum(10000)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_17.addWidget(self.horizontalSlider_2, 2, 1, 1, 3)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_14.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_archivo)
        self.menuArchivo.addAction(self.actionGuardar_archivo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir_archivo.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_archivo.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PARTICULAS", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"               X", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"        Y", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"         Y", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"        X", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.pushButton_Ordenar_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton_Ordenar_distancia.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.pushButton_Ordenar_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Insertar", None))
        self.pushButton_Agregar_Inicio.setText(QCoreApplication.translate("MainWindow", u" Inicio", None))
        self.pushButton_Agregar_Final.setText(QCoreApplication.translate("MainWindow", u" Final", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_Mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_Mostrar_Grafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de particula:", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Contador_label.setText(QCoreApplication.translate("MainWindow", u"Contador de particulas:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.pushButton_Kruskal.setText(QCoreApplication.translate("MainWindow", u"Usar", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.pushButton_Dijkstra.setText(QCoreApplication.translate("MainWindow", u"Usar", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Fuerza Bruta", None))
        self.pushButton_Fuerza_bruta.setText(QCoreApplication.translate("MainWindow", u"Usar", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.pushButton_Prim.setText(QCoreApplication.translate("MainWindow", u"Usar", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u" Puntos", None))
        self.Mostrar_puntos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar Puntos", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Graham", None))
        self.pushButton_Graham.setText(QCoreApplication.translate("MainWindow", u"Usar", None))
        self.limpiar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pushButton_dibujar_random.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Algoritmos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

