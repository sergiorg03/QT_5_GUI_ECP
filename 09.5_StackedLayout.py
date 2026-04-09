import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, \
    QStackedLayout
from UserControl import CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        # Layout en pila (Unos encima de otros)
        layout = QStackedLayout()

        # Stacked Layout  5 items
        layout.addWidget(CustomColorLabel("red", "0"))
        layout.addWidget(CustomColorLabel("green", "1"))
        layout.addWidget(CustomColorLabel("blue", "2"))
        layout.addWidget(CustomColorLabel("yellow", "3"))
        layout.addWidget(CustomColorLabel("cyan", "4"))

        layout.setCurrentIndex(2) # Elegimos el widget a mostrar

        widget = QWidget() # Creamos el widget
        widget.setLayout(layout) # Añadimos los layouts al widget para mostrarlo
        self.setCentralWidget(widget) # Añadimos el widget a la pantalla
































# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()