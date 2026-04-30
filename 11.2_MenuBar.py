import sys
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, \
    QStatusBar, QMessageBox, QFileDialog
from UserControl import CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(400, 400)
        # Su código aquí

        widget = CustomColorLabel("light blue", "Hello World")
        self.setCentralWidget(widget)

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
        button_actions_2 = QAction(QIcon("icons/icons/blue-folder-horizontal.png"), "&Cerrar...", self)
        button_actions_2.setStatusTip("Cerrar fichero")
        button_actions_2.triggered.connect(lambda: self.button_actions_clicked("Cerrar"))
        file_menu.addAction(button_actions_2)

        file_menu.addSeparator() # crea la línea separadora

        # Tercer action
        button_actions_3 = QAction(QIcon("icons/icons/application-icon.png"), "Ce&rrar aplicación", self)
        button_actions_3.setStatusTip("Cerrar aplicación ")
        button_actions_3.triggered.connect(lambda: self.button_actions_clicked("Cerrar aplicacion"))
        button_actions_3.setShortcut(QKeySequence("Ctrl+Q")) # Crea un atajo de teclado
        file_menu.addAction(button_actions_3)

        # Submenu
        file_submenu = file_menu.addMenu("&Submenu")
        button_actions_sm_1 = QAction(QIcon("icons/icons/network.png"), "&Red", self)
        button_actions_sm_1.setStatusTip("Menu de red --> Ethernet")
        button_actions_sm_1.triggered.connect(lambda: self.button_actions_clicked("Submenu Red"))
        file_submenu.addAction(button_actions_sm_1)

        button_actions_sm_2 = QAction(QIcon("icons/icons/network-ip-local.png"), "&Local", self)
        button_actions_sm_2.setStatusTip("Menu de red --> Local")
        button_actions_sm_2.triggered.connect(lambda: self.button_actions_clicked("Submenu Local"))
        file_submenu.addAction(button_actions_sm_2)


        # Fin de bloque de código
        self.setCentralWidget(widget)
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
            dialog.setNameFilter("Archivos pdf (*.pdf);;Todos los archivos (*.*)")
            if dialog.exec():
                filename = dialog.selectedFiles()[0]
                print(f"Ruta del fishero: {filename}")


# Punto de entrada de la App
app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()