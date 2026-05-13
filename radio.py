import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, \
    QStatusBar, QSlider, QDial
from UserControl import CustomColor, CustomColorLabel

# MainWindow
class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(800, 600)

        # Satus Bar
        statusBar = QStatusBar(self)
        self.setStatusBar(statusBar)

        layout = QVBoxLayout() # Layout general

        # Su código aquí

        layout1 = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        layout1.addWidget(self.slider)

        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.setValue(0)
        self.dial.valueChanged.connect(lambda: self.set_frecuency(self.dial.value()))
        layout1.addWidget(self.dial)
        
        
        layout.addLayout(layout1)

        # Fin de bloque de código
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_frecuency(self, frecuency):
        self.slider.setValue(frecuency)

# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()