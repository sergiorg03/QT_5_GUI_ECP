import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from UserControl import CustomColor

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        layout = QHBoxLayout()

        layout.addWidget(CustomColor('red'))
        layout.addWidget(CustomColor('green'))
        layout.addWidget(CustomColor("blue"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()