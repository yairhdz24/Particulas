#Autor Yair Hernandez Ochoa

from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow()

window.show()

sys.exit(app.exec_())

