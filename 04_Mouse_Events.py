import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit


class MainWindow(QMainWindow):

    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(600, 300)

        self.setMouseTracking(True) # Keep track of mouse

        self.label = QLabel("Click on the window", self) # Label (Texto, padre)
        self.setCentralWidget(self.label)
        self.label.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.label.setText(f"Mouse was moving at ({event.globalPos()})!")
        print(f"Mouse was moving at ({event.globalPos()})!")

    '''
    Metodos más importantes de los botones
    .button
    buttons
    Qt.LeftButton mascaras ->(001)
    Qt.rightButton mascara --> (010)
    Qt.MiddleButton mascara ->(100)
    Todos --> (111)
    .globalPos
    .globalX()
    .globalY() 
    .pas() --> posicion int
    .posF() --> posicion Float
    '''

    def mousePressEvent(self, event):
        self.label.setText(f"Mouse pressed with button ({event.buttons()})!")

    def mouseReleaseEvent(self, event):
        #self.label.setText("Mouse released!")
        print("Mouse released!")

    def mouseDoubleClickEvent(self, a0):
        self.label.setText("Mouse was doubled clicked!")


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()