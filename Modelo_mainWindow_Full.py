import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit,
    QCheckBox, QRadioButton, QComboBox, QSpinBox, QDoubleSpinBox,
    QSlider, QDial, QLCDNumber, QProgressBar,
    QDateEdit, QTimeEdit, QDateTimeEdit,
    QMenu, QAction, QStatusBar, QToolBar, QMenuBar,
    QMessageBox, QFileDialog, QListWidget, QTabWidget,
)
from UserControl import CustomColor, CustomColorLabel


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        # --- Configuración de la ventana ---
        self.setWindowTitle(title)
        self.setMinimumSize(800, 600)

        # --- Layout principal (cambiar a QHBoxLayout o QGridLayout si se necesita) ---
        layout = QVBoxLayout()

        # --- Widgets (tu código aquí) ---

        # --- Fin de bloque de widgets ---

        # --- Widget central ---
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # --- Barra de menús ---
        self._create_menu_bar()

        # --- Barra de herramientas ---
        self._create_tool_bar()

        # --- Barra de estado ---
        status_bar = QStatusBar(self)
        status_bar.showMessage("Listo")
        self.setStatusBar(status_bar)

    # =========================================================================
    # MENÚ
    # =========================================================================
    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        # ---- Menú Archivo ----
        file_menu = menu_bar.addMenu("&Archivo")

        act_open = QAction(QIcon("icons/icons/blue-folder-horizontal-open.png"), "&Abrir...", self)
        act_open.setStatusTip("Abrir archivo")
        act_open.setShortcut(QKeySequence("Ctrl+O"))
        act_open.triggered.connect(lambda: self._on_open_file())
        file_menu.addAction(act_open)

        act_save = QAction(QIcon("icons/icons/blue-folder-horizontal.png"), "&Guardar...", self)
        act_save.setStatusTip("Guardar archivo")
        act_save.setShortcut(QKeySequence("Ctrl+S"))
        act_save.triggered.connect(lambda: self._on_save_file())
        file_menu.addAction(act_save)

        file_menu.addSeparator()

        act_exit = QAction("&Salir", self)
        act_exit.setStatusTip("Cerrar la aplicación")
        act_exit.setShortcut(QKeySequence("Ctrl+Q"))
        act_exit.triggered.connect(self.close)
        file_menu.addAction(act_exit)

        # ---- Menú Editar ----
        edit_menu = menu_bar.addMenu("&Editar")

        act_undo = QAction("&Deshacer", self)
        act_undo.setShortcut(QKeySequence("Ctrl+Z"))
        act_undo.triggered.connect(lambda: self._on_action("Deshacer"))
        edit_menu.addAction(act_undo)

        act_redo = QAction("&Rehacer", self)
        act_redo.setShortcut(QKeySequence("Ctrl+Y"))
        act_redo.triggered.connect(lambda: self._on_action("Rehacer"))
        edit_menu.addAction(act_redo)

        # ---- Menú Ayuda ----
        help_menu = menu_bar.addMenu("&Ayuda")

        act_about = QAction("&Acerca de...", self)
        act_about.triggered.connect(lambda: self._on_about())
        help_menu.addAction(act_about)

    # =========================================================================
    # BARRA DE HERRAMIENTAS
    # =========================================================================
    def _create_tool_bar(self):
        toolbar = QToolBar("Barra de herramientas")
        toolbar.setIconSize(QSize(32, 32))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        act_new = QAction(QIcon("icons/icons/document.png"), "&Nuevo", self)
        act_new.setStatusTip("Crear nuevo")
        act_new.triggered.connect(lambda: self._on_action("Nuevo"))
        toolbar.addAction(act_new)

        act_open = QAction(QIcon("icons/icons/blue-folder-horizontal-open.png"), "&Abrir", self)
        act_open.setStatusTip("Abrir archivo")
        act_open.triggered.connect(lambda: self._on_open_file())
        toolbar.addAction(act_open)

        toolbar.addSeparator()

        act_save = QAction(QIcon("icons/icons/blue-folder-horizontal.png"), "&Guardar", self)
        act_save.setStatusTip("Guardar archivo")
        act_save.triggered.connect(lambda: self._on_save_file())
        toolbar.addAction(act_save)

        self.addToolBar(toolbar)

    # =========================================================================
    # HANDLERS
    # =========================================================================
    def _on_action(self, name):
        print(f"Acción: {name}")

    def _on_open_file(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Abrir archivo")
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Todos los archivos (*.*)")
        if dialog.exec():
            path = dialog.selectedFiles()[0]
            print(f"Archivo seleccionado: {path}")

    def _on_save_file(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Guardar archivo")
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilter("Todos los archivos (*.*)")
        if dialog.exec():
            path = dialog.selectedFiles()[0]
            print(f"Guardar en: {path}")

    def _on_about(self):
        QMessageBox.about(self, "Acerca de", "Mi aplicación")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow("Mi App")
    window.show()
    app.exec()
