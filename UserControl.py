from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget


class CustomColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)