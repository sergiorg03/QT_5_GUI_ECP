import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT5")
        self.setFixedSize(600,400)

        button = QPushButton("CocaCola")

        self.setCentralWidget(button)

# Punto de entrada de la App
app = QApplication(sys.argv)
# Creamos la ventana
window = MainWindow() # hacer que sea editable la pantalla
window.show() # mostramos los objetos, ya que por defecto están ocultos
# Ejecutamos la app
app.exec()