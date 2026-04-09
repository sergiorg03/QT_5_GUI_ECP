import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

# sudo apt install pyqut5, pyqt5-tools

class MainWindow(QMainWindow):

    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(600, 400)

        self.button = QPushButton("CocaCola")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.setWindowTitle("My One Shoot App")
        self.button.setText("You already clicked me")

        self.button.setDisabled(True)
        # ó
        #self.button.setEnabled(False)


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()