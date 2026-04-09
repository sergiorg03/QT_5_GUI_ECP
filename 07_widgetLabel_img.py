import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from UserControl import CustomColor

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(800, 600)

        '''self.label = QLabel("img")
        self.setCentralWidget(self.label)

        font = self.label.font()
        font.setPointSize(30)
        self.label.setFont(font)

        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Alineación al centro

        self.label.setPixmap(QPixmap("Patricio.jpg"))'''

        customColor = CustomColor("red")
        self.setCentralWidget(customColor)


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()