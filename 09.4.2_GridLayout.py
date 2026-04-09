import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout
from UserControl import CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        layout = QGridLayout()

        # Si elimino alguno se mantiene en su posición
        #layout.addWidget(CustomColorLabel("red", "0,0"), 0, 0)
        layout.addWidget(CustomColorLabel("green", "0,1"), 0, 1)
        layout.addWidget(CustomColorLabel("blue", "0,2"), 0, 2)
        layout.addWidget(CustomColorLabel("yellow", "1,0"), 1, 0)
        layout.addWidget(CustomColorLabel("cyan", "1,1"), 1, 1)
        #layout.addWidget(CustomColorLabel("magenta", "1,2"), 1, 2)
        layout.addWidget(CustomColorLabel("gray", "2,0"), 2, 0)
        #layout.addWidget(CustomColorLabel("orange", "2,1"), 2, 1)
        layout.addWidget(CustomColorLabel("purple", "2,2"), 2, 2)

        widget = QWidget() # Creamos el widget
        widget.setLayout(layout) # Añadimos los layouts al widget para mostrarlo
        self.setCentralWidget(widget) # Añadimos el widget a la pantalla
































# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()