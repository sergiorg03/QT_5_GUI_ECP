import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction


class MainWindow(QMainWindow):

    '''
    # Menú contextual por defecto
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(600, 300)

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        menu.addAction(QAction("CocaCola", self))
        menu.addAction(QAction("Pesi", self))
        menu.addAction(QAction("CR7", self))

        menu.exec_(event.globalPos())'''

    # Menú contextual customizados
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(600, 300)

        # Menús contextuales customizados
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        menu = QMenu(self)
        menu.addAction(QAction("CocaCola", self))
        menu.addAction(QAction("Pesi", self))
        menu.addAction(QAction("CR7", self))

        menu.exec_(self.mapToGlobal(pos))

# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()