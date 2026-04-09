import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from UserControl import CustomColor

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        layout = QVBoxLayout() #Layout generico

        # capas de layout
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout() # Layout simple
        layout3 = QHBoxLayout()

        layout1.addWidget(CustomColor('red'))
        layout1.addWidget(CustomColor('yellow'))
        layout1.addWidget(CustomColor("purple"))

        layout2.addWidget(CustomColor("green"))

        layout3.addWidget(CustomColor("red"))
        layout3.addWidget(CustomColor("purple"))

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()