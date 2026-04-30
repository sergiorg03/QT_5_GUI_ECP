import sys

from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, \
    QStatusBar, QMessageBox, QFileDialog, QLabel, QTextEdit
from UserControl import CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(400, 400)
        # Su código aquí

        self.TextEdit = QTextEdit(self)
        self.setCentralWidget(self.TextEdit)

        # Menú
        menu = self.menuBar() # Hereda de QMainWindow
        file_menu = menu.addMenu("&Fichero") # Entrada de menú. El & crea el atajo de teclado de la letra que precede en este caso la F
        file_menu.setStatusTip("Menu de ficheros")
        # Añadimos acciones
        # Primer action
        button_actions = QAction(QIcon("icons/icons/blue-folder-horizontal-open.png"), "&Abrir...", self)
        button_actions.setStatusTip("Abrir archivo")
        button_actions.triggered.connect(lambda: self.button_actions_clicked("Abrir fichero"))
        file_menu.addAction(button_actions) # Añadimos al menú el action

        # Segundo action
        button_actions_2 = QAction(QIcon("icons/icons/blue-folder-horizontal.png"), "&Guardar...", self)
        button_actions_2.setStatusTip("Guardar fichero")
        button_actions_2.triggered.connect(lambda: self.button_actions_clicked("Guardar fichero"))
        file_menu.addAction(button_actions_2)


        # Fin de bloque de código
        self.setStatusBar(QStatusBar(self))

    # Menu bar buttons handler
    def button_actions_clicked(self, s):
        print(s)
        if s == "Cerrar aplicacion":
            # Creamos el dialog
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Cerrar aplicación")
            dialog.setText("¿Desea cerrar la aplicación?")
            # Asignamos los botones del dialog
            dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dialog.setIcon(QMessageBox.Question)
            button = dialog.exec()
            if button == QMessageBox.Yes:
                app.quit() # ó self.close()

        elif s == "Abrir fichero":
            dialog = QFileDialog(self)
            dialog.setWindowTitle("Abrir fichero")
            dialog.setFileMode(QFileDialog.ExistingFiles)
            dialog.setNameFilter("Archivos de texto (*.txt);;Todos los archivos (*.*)")
            if dialog.exec():
                filename = dialog.selectedFiles()[0]
                print(f"Ruta del fishero: {filename}")

                self.TextEdit.setText(self.open_file(dialog.selectedFiles()[0]))
        elif s == "Guardar fichero":
            dialog = QFileDialog(self)
            dialog.setWindowTitle("Guardar fichero")
            dialog.setAcceptMode(QFileDialog.AcceptSave)
            dialog.setNameFilter("Archivos de texto (*.txt);;Todos los archivos (*.*)")
            if dialog.exec():
                self.save_file(dialog.selectedFiles()[0], self.TextEdit.toPlainText())

    def open_file(self, ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    def save_file(self, ruta, content):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(content)

    
# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("Notepad")
window.show()
app.exec()