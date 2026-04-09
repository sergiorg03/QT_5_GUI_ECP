import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, \
    QStackedLayout, QPushButton
from UserControl import CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        layout_main = QVBoxLayout()
        layout_button = QHBoxLayout()
        self.layout_tabs = QStackedLayout()

        button_1 = QPushButton("CocaCola")
        button_1.clicked.connect(lambda: self.change_tab(0))
        layout_button.addWidget(button_1)

        button_2 = QPushButton("Pesi")
        button_2.clicked.connect(lambda: self.change_tab(1))
        layout_button.addWidget(button_2)

        button_3 = QPushButton("CR7")
        button_3.clicked.connect(lambda: self.change_tab(2))
        layout_button.addWidget(button_3)

        layout_main.addLayout(layout_button) # Añadimos el layout de botones al layout principal

        # Stacked Layout  5 items
        self.layout_tabs.addWidget(CustomColorLabel("red", "0"))
        self.layout_tabs.addWidget(CustomColorLabel("green", "1"))
        self.layout_tabs.addWidget(CustomColorLabel("blue", "2"))
        self.layout_tabs.setCurrentIndex(0)

        layout_main.addLayout(self.layout_tabs)

        widget = QWidget() # Creamos el widget
        widget.setLayout(layout_main) # Añadimos los layouts al widget para mostrarlo
        self.setCentralWidget(widget) # Añadimos el widget a la pantalla



    def change_tab(self, indise):
        #print("Toma colacola sin verguenza")
        print(f"Mostramos el layaut con el indise: {indise}")
        self.layout_tabs.setCurrentIndex(indise)





























# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()