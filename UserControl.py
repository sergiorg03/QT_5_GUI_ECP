from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QWidget, QLCDNumber, QLabel

class CustomColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette) # Asiganamos el color de fondo

class CustomColorLabel(QLabel):
    def __init__(self, color, text):
        super().__init__()

        self.setAutoFillBackground(True)

        # Creamos la paleta de colores
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))

        self.setPalette(palette) # Asiganamos el color de fondo

        self.setText(text) # Añadimos el texto

        # Centrado de texto
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Tamaño del texto
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)