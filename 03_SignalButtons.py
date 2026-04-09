import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT5")
        self.setFixedSize(600, 400)

        button = QPushButton("CocaCola")
        button.clicked.connect(self.the_button_have_been_clicked)

        self.setCentralWidget(button)

    def the_button_have_been_clicked(self):
        print("Toma colacola sin verguenza")




# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()