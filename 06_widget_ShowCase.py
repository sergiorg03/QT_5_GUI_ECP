import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QCheckBox, QComboBox, QDialog, QDateEdit, \
    QDateTimeEdit, QDoubleSpinBox, QDial, QFontComboBox, QLCDNumber, QLabel, QVBoxLayout, QLineEdit, QProgressBar, \
    QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        # Añadimos las instancias de los widgets al layout
        for w in widgets:
            layout.addWidget(w()) # Con el () llamamos al constructor de la misma, si no, estaríamos añadiendo referencias de las clases al layout

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()