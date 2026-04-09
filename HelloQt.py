import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Creamos la instancia de la app
app = QApplication(sys.argv)

# Creamos la ventana
#window = QWidget()
#window = QPushButton("CocaCola")
window = QMainWindow("Hello World") # hacer que sea editable la pantalla


window.show() # mostramos los objetos, ya que por defecto están ocultos

# Ejecutamos la app
app.exec()