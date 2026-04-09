import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QToolBar, \
    QActionGroup, QAction, QStatusBar
from UserControl import CustomColor, CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        # Su código aquí

        # Fin del bloque de código
        widget = CustomColorLabel("light blue", "Hello World")
        self.setCentralWidget(widget)

        # Menú Bar
        toolbar = QToolBar("Mai tulbar")
        toolbar.setIconSize(QSize(32, 32))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        button_actions = QAction(QIcon("icons/icons/document.png"), "Fichero", self)
        button_actions.setStatusTip("Esto es pa los fisheros")
        button_actions.triggered.connect(lambda: self.button_actions_clicked("Fishero"))
        toolbar.addAction(button_actions)

        button_actions_2 = QAction(QIcon("icons/icons/smiley-sleep.png"), "A&iuda", self)
        button_actions_2.setStatusTip("Aiudaaaaaaaa")
        button_actions_2.triggered.connect(lambda: self.button_actions_clicked("CocaCola"))
        toolbar.addAction(button_actions_2)

        button_actions_3 = QAction(QIcon("icons/icons/smiley-sleep.png"), "&Mirmi", self)
        button_actions_3.setStatusTip("Irse a mirmi")
        button_actions_3.triggered.connect(lambda: self.button_actions_clicked("Vete a mirmiiii"))
        toolbar.addAction(button_actions_3)

        # Assign menu bar status bar to main window
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))


    # Menu bar buttons handler
    def button_actions_clicked(self, s):
        print(s)

















# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("Menú App")
window.show()
app.exec()