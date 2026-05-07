# Caja registradora con billetes de vuelta infinitos
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, \
    QDoubleSpinBox, QPushButton, QMessageBox, QListWidget, QListView, QTableView
from UserControl import CustomColor, CustomColorLabel

def calcular_cambio_monedas(importe_productos, cantidad_cliente):
    # Calcular el cambio a devolver
    cambio = round(cantidad_cliente - importe_productos, 2)

    cambio_inicial = cambio

    MONEDAS = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cambio_a_devolver = {}

    # Comprobar si se le devuelve
    if cambio < 0: # Debe pagar más
        raise ValueError(f"ERROR: El cliente no ha dado suficiente dinero. Faltante: {abs(cambio)} €.")
    elif cambio == 0: # Ha pagado el importe justo
        return cambio_a_devolver, cambio_inicial
    else: # Devolver cambio
        #print(f"El cambio a devolver es: {cambio}")
        for moneda in MONEDAS:
            if cambio >= moneda: # Comprobamos que el cambio es mayor que la moneda elegida
                cantidad_monedas = int(cambio // moneda) # Obtenemos el número de monedas que podemos devolver
                cambio_a_devolver[moneda] = cantidad_monedas # añadimos la moneda al diccionario
                cambio = round(cambio - cantidad_monedas * moneda, 2) # actualizamos el cambio
        return cambio_a_devolver, cambio_inicial

FONT_SIZE = 15
MIN_VALUE, MAX_VALUE = 0, 9999

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setFixedSize(400, 400)
        self.set_widget_font(self, font_size=FONT_SIZE)
        # Su código aquí

        layoutV = QVBoxLayout()
        layoutH1 = QHBoxLayout()
        layoutH2 = QHBoxLayout()
        layoutH3 = QHBoxLayout()
        layoutH90 = QHBoxLayout()
        layoutH99 = QHBoxLayout()

        # LayoutH01 - Importe
        l_importe = QLabel("Importe: ")
        l_importe.setAlignment(Qt.AlignCenter)
        self.set_widget_font(l_importe, FONT_SIZE)
        layoutH1.addWidget(l_importe)

        self.w_importe_prod = QDoubleSpinBox()
        self.set_widget_font(self.w_importe_prod, FONT_SIZE)
        self.w_importe_prod.setAlignment(Qt.AlignVCenter)
        self.w_importe_prod.setRange(MIN_VALUE, MAX_VALUE)
        #asignamos el spin al layouth01
        layoutH1.addWidget(self.w_importe_prod)

        # LayoutH2 - Entregado
        l_entrega_cli = QLabel("Pagado: ")
        l_entrega_cli.setAlignment(Qt.AlignCenter)
        self.set_widget_font(l_entrega_cli, FONT_SIZE)
        layoutH2.addWidget(l_entrega_cli)

        self.w_cantidad_cli = QDoubleSpinBox()
        self.set_widget_font(self.w_cantidad_cli, FONT_SIZE)
        self.w_cantidad_cli.setAlignment(Qt.AlignVCenter)
        self.w_cantidad_cli.setRange(MIN_VALUE, MAX_VALUE)
        # asignamos el spin al layouth01
        layoutH2.addWidget(self.w_cantidad_cli)

        # LayoutH3 - Devolución
        l_devolucion = QLabel("A Devolver: ")
        l_devolucion.setAlignment(Qt.AlignCenter)
        self.set_widget_font(l_devolucion, FONT_SIZE)
        layoutH3.addWidget(l_devolucion)

        self.w_cantidad_dev = QDoubleSpinBox()
        self.set_widget_font(self.w_cantidad_dev, FONT_SIZE)
        self.w_cantidad_dev.setAlignment(Qt.AlignVCenter)
        self.w_cantidad_dev.setRange(MIN_VALUE, MAX_VALUE)
        self.w_cantidad_dev.setEnabled(False)
        # asignamos el spin al layouth01
        layoutH3.addWidget(self.w_cantidad_dev)

        # LayoutH90 - tabla de monedas (usar QTableView con modelo de dos columnas)
        self.lista_monedas = QTableView()
        self.model = QStandardItemModel(0, 2, self)  # 0 rows, 2 columns
        self.model.setHorizontalHeaderLabels(["Billete/Moneda", "Cantidad"])
        self.lista_monedas.setModel(self.model)
        self.lista_monedas.horizontalHeader().setStretchLastSection(True)
        self.lista_monedas.setEditTriggers(QTableView.NoEditTriggers)
        # Populate initial rows with denominations and zero quantity
        self.denominations = ["500.0€", "200.0€", "100.0€", "50.0€", "20.0€", "10.0€", "5.0€", "2.0€", "1.0€", "0.5€", "0.2€",
                              "0.1€", "0.05€", "0.02€", "0.01€"]
        # Populate initial rows with zero quantities
        for moneda in self.denominations:
            item_moneda = QStandardItem(moneda)
            item_cantidad = QStandardItem("0")
            self.model.appendRow([item_moneda, item_cantidad])


        # IA
        # self.lista_monedas = QTableView()
        # self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(["Billete/Moneda", "Cantidad"])
        # self.lista_monedas.setModel(self.model)
        # self.lista_monedas.horizontalHeader().setStretchLastSection(True)

        layoutH90.addWidget(self.lista_monedas)


        # LayoutH99 - Botonera
        self.btn_calcular = QPushButton("Calcular")
        self.btn_calcular.clicked.connect(self.onclick_calcular)
        self.set_widget_font(self.btn_calcular, FONT_SIZE)
        layoutH99.addWidget(self.btn_calcular)


        # Añadimos los layouts al layaout principal
        layoutV.addLayout(layoutH1)
        layoutV.addLayout(layoutH2)
        layoutV.addLayout(layoutH3)
        layoutV.addLayout(layoutH90)
        layoutV.addLayout(layoutH99)

        # Fin de bloque de código
        # Widget genérico para asignar a la ventana
        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)

    def set_widget_font(self, widget, font_size):
        font = widget.font()
        font.setPointSize(font_size)
        widget.setFont(font)

    def onclick_calcular(self):
        try:
            self.cambio_dict, cambio_total = calcular_cambio_monedas(self.w_importe_prod.value(), self.w_cantidad_cli.value())
            # If both importe and pago are zero, show info and skip further processing
            if self.w_importe_prod.value() == 0 and self.w_cantidad_cli.value() == 0:
                self.show_dialog("Importe y pago son 0. No hay cambio.", "Información", QMessageBox.Information)
                self.w_cantidad_dev.setValue(0)  # No change
            else:
                self.w_cantidad_dev.setValue(cambio_total)  # Asignamos el valor al QDoubleSpinBox

                # Actualizar el modelo de la tabla con el cambio calculado
                # Update table with all denominations, showing quantity to give (0 if none)
                self.model.setRowCount(0)  # clear existing rows
                any_change = False
                for moneda_str in self.denominations:
                    # Convert string like "500.0€" to numeric value for lookup
                    valor = float(moneda_str.replace('€', ''))
                    cantidad = self.cambio_dict.get(valor, 0)
                    if cantidad > 0:
                        any_change = True
                        item_moneda = QStandardItem(moneda_str)
                        item_moneda.setTextAlignment(Qt.AlignCenter)
                        item_cantidad = QStandardItem(str(cantidad))
                        item_cantidad.setTextAlignment(Qt.AlignCenter)
                        self.model.appendRow([item_moneda, item_cantidad])
                if not any_change:
                    # No denominations to return; show informational dialog
                    self.show_dialog("No hay cambio para devolver.", "Información", QMessageBox.Information)

        except ValueError as e:
            # QMessageBox.warning(self, "Error de pago. Dinero faltante", f"{str(e)}")
            self.show_dialog(f"{e}", "Error: Dinero insuficiente.")

    def show_dialog(self, texto: str, title: str = "Error", icon=QMessageBox.Critical):
        dialog = QMessageBox(self)
        self.set_widget_font(dialog, FONT_SIZE)
        dialog.setWindowTitle(title)
        dialog.setIcon(icon)
        dialog.setText(texto)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.exec()



    # Punto de entrada de la App

app = QApplication(sys.argv)
window = MainWindow("Caja Registradora")
window.show()
app.exec()