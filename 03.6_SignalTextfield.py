import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit


class MainWindow(QMainWindow):

    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(400, 300)

        self.label = QLabel("Prueba", self) # Label (Texto, padre)
        #self.setCentralWidget(self.label) # Añadimos el widget a la ventana
        self.label.setFixedSize(200, 30)
        self.label.move(20, 20)

        self.input_text = QLineEdit("Prueba", self) # Input Text Field (Texto, padre)
        #self.setCentralWidget(self.input_text) # Añadimos el input text a la ventana
        self.input_text.setFixedSize(200, 60)
        self.input_text.move(20, 60)

        self.input_text.textChanged.connect(self.change_text)
        # ó que lo escriba directamente en el label
        #self.input_text.textChanged.connect(self.label.setText)

        '''Para añadir los dos componentes a la ventana hay que indicar el padre en el constructor de los elementos (Texto, padre) y situarlos en posiciones diferentes. '''


    def change_text(self):
        text = self.input_text.text()
        self.label.setText(text)
        print(text)

# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()