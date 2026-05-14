import random
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, \
    QPushButton, QToolBar, QAction, QTextEdit, QDial, QSlider, QStatusBar, QTabWidget
from UserControl import CustomColor, CustomColorLabel

FONT_SIZE = 15

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(800, 600)
        # Su código aquí

        # Se crea la toolbar (Menu de arriba BASICO)
        """toolbar = QToolBar()
        toolbar.setIconSize(QSize(48, 48))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # Se configuran las acciones de la toolbar
        action = QAction(QIcon("icons/icons/poop.png"), "&Poop", self) # definimos el icono de la accion
        action.setStatusTip("Status de la accion. ")
        action.setShortcut("Ctrl+Q") # Atajo de teclado

        toolbar.addAction(action) # Añadimos la accion al toolbar
        self.addToolBar(toolbar) # se añade la toolbar"""

        # Menú
        menu = self.menuBar()
        poop = menu.addMenu("&Poop")
        poop.setStatusTip("Menú poop")

        # Acciones del menú
        buton_action1 = QAction(QIcon("icons/icons/poop.png"), "&Abrir poop", self)
        buton_action1.setStatusTip("Status tip del boton de abrir. ")
        buton_action1.triggered.connect(lambda: self.funsion_menu("Ji onbre, que me queo zin come "))
        poop.addAction(buton_action1)

        # Satus Bar
        statusBar = QStatusBar(self)
        self.setStatusBar(statusBar)

        layout = QVBoxLayout() # Layout principal
        layout99 = QHBoxLayout() # Último Layout

        self.label = QLabel()
        self.set_widget_font(self.label, FONT_SIZE)
        layout99.addWidget(self.label)

        layouth1 = QHBoxLayout()

        button1 = QPushButton("Boton")
        self.set_widget_font(button1, FONT_SIZE)
        button1.clicked.connect(lambda: self.cagonto(f"Esto es el envio de texto mediante el lambda número {random.randint(0, 100)}. ")) # Si la funcion tiene parametros
        #button1.clicked.connect(self.cagonto) # Si la funcion no tiene parametros
        layouth1.addWidget(button1)

        layouth2 = QHBoxLayout()

        self.textEdit = QTextEdit()
        self.set_widget_font(button1, FONT_SIZE)
        self.textEdit.setFixedSize(QSize(200, 100))

        self.textEdit.textChanged.connect(lambda: self.cagonto(text=self.textEdit.toPlainText())) # Modificar un valor a la vez que se escribe

        layouth2.addWidget(self.textEdit)

        layouth3 = QHBoxLayout()

        dial = QDial()
        dial.setFixedSize(QSize(150, 150))
        dial.valueChanged.connect(lambda: self.cagonto(text=str(dial.value()))) # Muestra valores númericos en un label
        dial.setMaximum(1002) # Define el Máximo
        dial.setMinimum(-205) # Define el Mínimo
        layouth3.addWidget(dial)

        slider = QSlider(Qt.Horizontal)
        slider.setFixedSize(QSize(80, 30))
        slider.setMinimum(0)
        slider.setMaximum(200)
        slider.valueChanged.connect(lambda: self.cagonto(text=str(slider.value())))
        layouth3.addWidget(slider)

        # TABS diferentes colores (Hereda de QLABEL)
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)  # Cambiar la posición de las tabs
        tabs.setMovable(True)  # Permitir que se muevan las tabs

        for n, color in enumerate(["red", "green", "blue"]):
            tabs.addTab(CustomColorLabel(color, f"Tab {n}"), color)

        layout.addWidget(tabs)

        # TABS diferentes colores (Hereda de Qlayout)
        """for n, color in enumerate(["red", "green", "blue"]):
            
            tabs = QWidget()
            #tabs.setTabPosition(QTabWidget.West)  # Cambiar la posición de las tabs
            #tabs.setMovable(True)  # Permitir que se muevan las tabs
            
            # Añadimos un label a la pestaña
            tabs_lay = QVBoxLayout()
            tabs_lay.addWidget(QLabel(f"Contenido de la pestaña {color}"))
            
            # Añadimos un boton a la pestaña
            buton = QPushButton(f"Boton de la pestaña {color}")
            buton.clicked.connect(lambda: self.cagonto(text=f"Boton de la pestaña {color}"))
            tabs_lay.addWidget(buton)
            
            tabs.setLayout(tabs_lay)
            layout.addWidget(tabs) # añadimos las pestañas al layout"""

        layouth4 = QHBoxLayout()

        # Grid Layout
        grid = QGridLayout()
        grid.addWidget(CustomColorLabel("red", "Grid Layout"), 0, 0)
        grid.addWidget(CustomColorLabel("green", "Grid Layout"), 0, 1)
        #grid.addWidget(CustomColorLabel("yellow", "Grid Layout"), 1, 0)
        grid.addWidget(CustomColorLabel("blue", "Grid Layout"), 1, 1)
        b = QPushButton("AddWidget to Grid")
        b.clicked.connect(lambda: self.cagonto(text="AddWidget to grid"))
        grid.addWidget(b, 2, 0, 1, 2) # fila, columna, rowspan, colspan

        layouth4.addLayout(grid)

        # Layouts
        layout.addLayout(layouth1)
        layout.addLayout(layouth2)
        layout.addLayout(layouth3)
        layout.addLayout(layouth4)
        layout.addLayout(layout99)

        # Fin de bloque de código
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def cagonto(self, text):
        #print(f"CAGONTO y {text}")
        self.label.setText(text)
        self.setStatusTip(text)

    def set_widget_font(self, widget, font_size):
        font = widget.font()
        font.setPointSize(font_size)
        widget.setFont(font)

    def funsion_menu(self, testo):
        print(testo)
        self.setStatusTip(testo)


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("Tituloooo")
window.show()
app.exec()