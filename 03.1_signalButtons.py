import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT5")
        self.setFixedSize(600, 400)

        self.button = QPushButton("CocaCola")
        #self.button.clicked.connect(self.the_button_have_been_clicked)

        #self.button.setCheckable(True) # Los botones se pueden checkable pk tienen los mismos atributos que los checkbutton
        #self.button.clicked.connect(self.the_button_was_toggled)

        self.button.released.connect(self.the_button_was_released)


        self.setCentralWidget(self.button)

    def the_button_have_been_clicked(self):
        print("Toma colacola sin verguenza")

    def the_button_was_toggled(self, checked):
        print(f"Checked: {checked}")

    def the_button_was_released(self):
        print(f"El boton fue releaseado {self.button.isChecked()}")

# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()