import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, \
    QStackedLayout, QPushButton, QTabWidget
from UserControl import CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West) # Cambiar la posición de las tabs
        tabs.setMovable(True) # Permitir que se muevan las tabs 

        for n, color in enumerate(["red", "green", "blue"]):
            tabs.addTab(CustomColorLabel(color, f"Tab {n}"), color)


        self.setCentralWidget(tabs) # Añadimos el widget a la pantalla

# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()