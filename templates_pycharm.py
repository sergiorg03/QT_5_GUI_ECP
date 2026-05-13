# ============================================================================
# LIVE TEMPLATES QT5 - WIDGETS CON TODOS SUS MÉTODOS MÁS USADOS
# ============================================================================
"""
Plantillas con widgets completos y sus métodos más utilizados.
Cada widget incluye: creación + configuración + métodos principales + señales.
"""

import sys

from PyQt5.QtCore import Qt, QSize, QDate, QTime, QDateTime
from PyQt5.QtGui import QPixmap, QIcon, QKeySequence, QStandardItemModel, QStandardItem, QFont, QPalette, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit,
    QCheckBox, QRadioButton, QComboBox, QSpinBox, QDoubleSpinBox,
    QSlider, QDial, QLCDNumber, QProgressBar,
    QDateEdit, QTimeEdit, QDateTimeEdit, QFontComboBox,
    QMenu, QAction, QStatusBar, QToolBar, QMenuBar,
    QMessageBox, QFileDialog, QDialog,
    QListWidget, QTableView, QListView, QListWidgetItem,
    QTabWidget, QSizePolicy
)
from UserControl import CustomColor, CustomColorLabel

FONT_SIZE = 15


# ============================================================================
# FUNCIONES HELPER
# ============================================================================

def set_widget_font(widget, font_size):
    """Establece el tamaño de fuente de un widget."""
    font = widget.font()
    font.setPointSize(font_size)
    widget.setFont(font)


def connect_lambda(obj, signal, func, *args):
    """Conecta una señal a una lambda con parámetros."""
    if args:
        obj.signal.connect(lambda *a: func(*args))
    else:
        obj.signal.connect(func)


# ============================================================================
# QPUSHBUTTON
# ============================================================================
# Template: pushbutton
# ============================================================================
button = QPushButton("Texto del botón")
set_widget_font(button, FONT_SIZE)
button.clicked.connect(lambda: self.funcion("param"))

# --- MÉTODOS COMUNES ---
button.setText("Nuevo texto")                    # Establece el texto
button.text()                                    # Obtiene el texto
button.setIcon(QIcon("icon.png"))               # Establece icono
button.setIconSize(QSize(24, 24))              # Tamaño del icono
button.setFlat(True)                            # Botón sin borde
button.setDefault(True)                         # Botón por defecto (Enter)
button.setAutoDefault(True)                     # Auto-default en diálogos
button.setCheckable(True)                       # Modo toggle
button.setChecked(True)                         # Marcar/demarkar
button.isChecked()                              # Devuelve si está marcado
button.setEnabled(False)                        # Habilitar/deshabilitar
button.isEnabled()                              # Devuelve si está habilitado
button.setToolTip("Tooltip")                   # Tooltip al pasar el ratón
button.setShortcut("Ctrl+B")                   # Atajo de teclado
button.animateClick()                          # Simula click con animación
button.click()                                  # Simula click sin animación

# --- SEÑALES ---
# button.clicked.connect(...)                   # Al hacer click
# button.pressed.connect(...)                   # Al presionar
# button.released.connect(...)                  # Al soltar
# button.toggled.connect(...)                   # Al cambiar estado (checkable)

layout.addWidget(button)


# ============================================================================
# QCHECKBOX
# ============================================================================
# Template: checkbox
# ============================================================================
checkbox = QCheckBox("Texto del checkbox")
set_widget_font(checkbox, FONT_SIZE)
checkbox.stateChanged.connect(lambda state: self.check_funcion(state))

# --- MÉTODOS COMUNES ---
checkbox.setText("Nuevo texto")                 # Establece el texto
checkbox.text()                                 # Obtiene el texto
checkbox.setChecked(True)                       # Marcar checkbox
checkbox.isChecked()                           # Devuelve si está marcado (True/False)
checkbox.setCheckState(Qt.Checked)             # Estado: Qt.Unchecked, Qt.PartiallyChecked, Qt.Checked
checkbox.checkState()                          # Devuelve estado (0, 1, 2)
checkbox.setTristate(True)                     # Permite 3 estados
checkbox.setEnabled(False)                     # Habilitar/deshabilitar
checkbox.isEnabled()                           # Devuelve si está habilitado
checkbox.setToolTip("Tooltip")                # Tooltip
checkbox.setShortcut("Ctrl+K")                # Atajo de teclado
checkbox.setFocus()                            # Dar foco

# --- Métodos de estado ---
# checkbox.setCheckState(Qt.Unchecked)         # 0 - Sin marcar
# checkbox.setCheckState(Qt.PartiallyChecked)  # 1 - Semi marcado
# checkbox.setCheckState(Qt.Checked)           # 2 - Marcado

# --- SEÑALES ---
# checkbox.stateChanged.connect(lambda state: ...)  # state: 0, 1, 2
# checkbox.clicked.connect(lambda checked: ...)     # checked: True/False
# checkbox.toggled.connect(lambda checked: ...)     # checked: True/False

layout.addWidget(checkbox)


# ============================================================================
# QRADIOBUTTON
# ============================================================================
# Template: radiobutton
# ============================================================================
radio = QRadioButton("Texto de la opción")
set_widget_font(radio, FONT_SIZE)
radio.toggled.connect(lambda checked: self.radio_funcion(checked) if checked else None)

# --- MÉTODOS COMUNES ---
radio.setText("Nuevo texto")                   # Establece el texto
radio.text()                                    # Obtiene el texto
radio.setChecked(True)                         # Seleccionar radio
radio.isChecked()                              # Devuelve si está seleccionado
radio.setAutoExclusive(False)                  # Desactiva exclusividad automática
radio.setEnabled(False)                        # Habilitar/deshabilitar
radio.isEnabled()                              # Devuelve si está habilitado
radio.setToolTip("Tooltip")                   # Tooltip

# --- SEÑALES ---
# radio.toggled.connect(lambda checked: ...)   # checked: True/False
# radio.clicked.connect(lambda checked: ...)   # checked: True/False

layout.addWidget(radio)


# ============================================================================
# QCOMBOBOX
# ============================================================================
# Template: combobox
# ============================================================================
combobox = QComboBox()
set_widget_font(combobox, FONT_SIZE)
combobox.currentIndexChanged.connect(lambda index: self.combo_funcion(index))

# --- MÉTODOS COMUNES ---
combobox.addItem("Opción 1")                   # Añade una opción
combobox.addItems(["Opción 2", "Opción 3"])   # Añade varias opciones
combobox.insertItem(0, "Insertar")            # Inserta en índice específico
combobox.removeItem(0)                        # Elimina opción por índice
combobox.clear()                               # Elimina todas las opciones
combobox.setCurrentIndex(0)                   # Selecciona por índice
combobox.currentIndex()                       # Devuelve índice actual
combobox.currentText()                        # Devuelve texto seleccionado
combobox.setCurrentText("Texto")              # Busca y selecciona texto
combobox.count()                              # Número de opciones
combobox.itemText(0)                          # Texto de un índice
combobox.itemData(0)                          # Dato asociado a un índice
combobox.setItemText(0, "Nuevo texto")        # Cambia texto de índice
combobox.setItemData(0, "dato")               # Establece dato a índice
combobox.findText("Texto")                    # Busca texto, devuelve índice o -1
combobox.findData("dato")                    # Busca dato, devuelve índice o -1
combobox.setEditable(True)                    # Permite edición
combobox.setMaxCount(10)                      # Máximo de opciones
combobox.setPlaceholderText("Seleccione...")  # Texto cuando está vacío
combobox.setEnabled(False)                    # Habilitar/deshabilitar
combobox.setToolTip("Tooltip")               # Tooltip

# --- SEÑALES ---
# combobox.currentIndexChanged.connect(lambda index: ...)   # Índice cambió
# combobox.currentTextChanged.connect(lambda text: ...)    # Texto cambió
# combobox.activated.connect(lambda index: ...)           # Usuario selecciona

layout.addWidget(combobox)


# ============================================================================
# QLABEL
# ============================================================================
# Template: label
# ============================================================================
label = QLabel("Texto del label")
set_widget_font(label, FONT_SIZE)
label.setAlignment(Qt.AlignCenter)

# --- MÉTODOS COMUNES ---
label.setText("Nuevo texto")                   # Establece el texto
label.text()                                    # Obtiene el texto
label.setAlignment(Qt.AlignCenter)            # Alineación: AlignLeft, AlignRight, AlignHCenter, AlignVCenter
label.setPixmap(QPixmap("imagen.png"))        # Establece imagen
label.pixmap()                                 # Devuelve imagen actual
label.clear()                                  # Limpia el texto
label.setWordWrap(True)                       # Ajuste de línea automático
label.setIndent(10)                          # Sangría
label.setMargin(5)                           # Margen interno
label.setStyleSheet("color: red;")           # Estilo CSS
label.setOpenExternalLinks(True)             # Abre enlaces en texto HTML
label.setTextFormat(Qt.PlainText)            # Formato: PlainText, RichText

# --- SEÑALES ---
# label.linkActivated.connect(lambda url: ...)  # Enlace clickeado (con HTML)

layout.addWidget(label)


# ============================================================================
# QLABEL CON IMAGEN
# ============================================================================
# Template: labelimg
# ============================================================================
label_img = QLabel()
pixmap = QPixmap("ruta/imagen.png")
pixmap_scaled = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
label_img.setPixmap(pixmap_scaled)

# --- MÉTODOS COMUNES ---
label_img.setPixmap(QPixmap("nueva.png"))    # Cambia la imagen
label_img.pixmap()                            # Obtiene imagen actual
label_img.clear()                             # Limpia la imagen
label_img.setScaledContents(True)             # Escala contenido para llenar
label_img.setAlignment(Qt.AlignCenter)        # Alineación

layout.addWidget(label_img)


# ============================================================================
# QLINEEDIT
# ============================================================================
# Template: lineedit
# ============================================================================
lineedit = QLineEdit()
set_widget_font(lineedit, FONT_SIZE)
lineedit.setPlaceholderText("Escribe aquí...")
lineedit.textChanged.connect(lambda text: self.line_funcion(text))

# --- MÉTODOS COMUNES ---
lineedit.setText("Texto inicial")            # Establece texto
lineedit.text()                               # Obtiene texto actual
lineedit.setPlaceholderText("Placeholder")   # Texto gris hint
lineedit.placeholderText()                    # Devuelve placeholder
lineedit.setMaxLength(50)                    # Longitud máxima
lineedit.maxLength()                         # Devuelve longitud máxima
lineedit.setReadOnly(True)                   # Solo lectura
lineedit.isReadOnly()                        # Devuelve si es solo lectura
lineedit.setEnabled(False)                   # Habilitar/deshabilitar
lineedit.isEnabled()                          # Devuelve si está habilitado
lineedit.selectAll()                         # Selecciona todo el texto
lineedit.setSelection(0, 5)                   # Selecciona rango (inicio, longitud)
lineedit.selectedText()                      # Devuelve texto seleccionado
lineedit.setEchoMode(QLineEdit.Password)     # Modo: Normal, Password, NoEcho
lineedit.echoMode()                          # Devuelve modo actual
lineedit.clear()                             # Limpia el campo
lineedit.copy()                              # Copia texto seleccionado
lineedit.cut()                               # Corta texto seleccionado
lineedit.paste()                             # Pega del portapapeles
lineedit.undo()                              # Deshace
lineedit.redo()                              # Rehace
lineedit.setAlignment(Qt.AlignCenter)        # Alineación del texto
lineedit.setFont(QFont("Arial", 12))         # Fuente
lineedit.setToolTip("Tooltip")              # Tooltip
lineedit.setFocus()                          # Da foco

# --- VALIDADORES ---
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
lineedit.setValidator(QIntValidator(0, 100))  # Solo números 0-100
lineedit.setValidator(QDoubleValidator(0.0, 100.0, 2))  # Decimales con 2 decimales

# --- MÁSCARA DE ENTRADA ---
lineedit.setInputMask("999.999.999.999")     # Máscara de IP

# --- SEÑALES ---
# lineedit.textChanged.connect(lambda text: ...)       # Texto cambió
# lineedit.textEdited.connect(lambda text: ...)        # Texto editado (no en setText)
# lineedit.returnPressed.connect(...)                  # Enter presionado
# lineedit.editingFinished.connect(...)                # Terminó edición
# lineedit.selectionChanged.connect(...)               # Selección cambió

layout.addWidget(lineedit)


# ============================================================================
# QTEXTEDIT
# ============================================================================
# Template: textedit
# ============================================================================
textedit = QTextEdit()
set_widget_font(textedit, FONT_SIZE)
textedit.setFixedSize(QSize(200, 100))
textedit.textChanged.connect(lambda: self.text_funcion(textedit.toPlainText()))

# --- MÉTODOS COMUNES ---
textedit.setText("Texto inicial")            # Establece texto
textedit.toPlainText()                       # Obtiene texto plano
textedit.setHtml("<b>HTML</b>")             # Establece HTML
textedit.toHtml()                           # Obtiene como HTML
textedit.append("Nuevo párrafo")            # Añade texto al final
textedit.clear()                             # Limpia todo
textedit.setReadOnly(True)                  # Solo lectura
textedit.isReadOnly()                       # Devuelve si es solo lectura
textedit.setEnabled(False)                  # Habilitar/deshabilitar
textedit.setFont(QFont("Arial", 12))       # Fuente
textedit.setTextColor(QColor("red"))        # Color del texto
textedit.setTextBackgroundColor(QColor("yellow"))  # Color de fondo del texto
textedit.setAlignment(Qt.AlignCenter)      # Alineación
textedit.setLineWrapMode(QTextEdit.WidgetWidth)  # Modo de ajuste
textedit.setPlaceholderText("Escribe aquí...")  # Placeholder (Qt5.2+)
textedit.selectAll()                        # Selecciona todo
textedit.copy()                             # Copia
textedit.cut()                              # Corta
textedit.paste()                           # Pega
textedit.undo()                            # Deshace
textedit.redo()                            # Rehace

# --- OBTENER/ESTABLECER POSICIÓN DEL CURSOR ---
cursor = textedit.textCursor()
cursor.movePosition(cursor.Start)
textedit.setTextCursor(cursor)

# --- SEÑALES ---
# textedit.textChanged.connect(...)                  # Contenido cambió
# textedit.copyAvailable.connect(lambda yes: ...)    # Texto disponible para copiar
# textedit.selectionChanged.connect(...)             # Selección cambió
# textedit.cursorPositionChanged.connect(...)        # Cursor cambió de posición

layout.addWidget(textedit)


# ============================================================================
# QSPINBOX
# ============================================================================
# Template: spinbox
# ============================================================================
spinbox = QSpinBox()
set_widget_font(spinbox, FONT_SIZE)
spinbox.setRange(0, 100)
spinbox.setValue(50)
spinbox.valueChanged.connect(lambda value: self.spin_funcion(value))

# --- MÉTODOS COMUNES ---
spinbox.setValue(75)                        # Establece valor
spinbox.value()                             # Obtiene valor actual
spinbox.setMinimum(0)                        # Valor mínimo
spinbox.minimum()                           # Devuelve mínimo
spinbox.setMaximum(100)                      # Valor máximo
spinbox.maximum()                           # Devuelve máximo
spinbox.setRange(0, 100)                    # Establece rango [min, max]
spinbox.setSingleStep(5)                    # Paso de incremento
spinbox.singleStep()                       # Devuelve paso
spinbox.setPrefix("$")                      # Prefijo (ej: "$")
spinbox.prefix()                           # Devuelve prefijo
spinbox.setSuffix(" €")                    # Sufijo (ej: "€")
spinbox.suffix()                           # Devuelve sufijo
spinbox.setReadOnly(True)                   # Solo lectura
spinbox.setWrapping(True)                   # Vuelve al inicio al pasar máximo
spinbox.setButtonSymbols(QSpinBox.PlusMinus)  # Símbolos: UpDownArrows, PlusMinus, NoButtons
spinbox.cleanText()                        # Texto sin prefijo/sufijo
spinbox.setAlignment(Qt.AlignCenter)        # Alineación del valor
spinbox.setEnabled(False)                   # Habilitar/deshabilitar
spinbox.setToolTip("Tooltip")              # Tooltip

# --- SEÑALES ---
# spinbox.valueChanged.connect(lambda value: ...)  # Valor cambió (int)
# spinbox.valueChanged.connect(lambda text: ...)    # Valor cambió (str)
# spinbox.editingFinished.connect(...)             # Terminó edición

layout.addWidget(spinbox)


# ============================================================================
# QDOUBLESPINBOX
# ============================================================================
# Template: doublespinbox
# ============================================================================
doublespin = QDoubleSpinBox()
set_widget_font(doublespin, FONT_SIZE)
doublespin.setRange(0.0, 999.99)
doublespin.setValue(25.50)
doublespin.setDecimals(2)
doublespin.valueChanged.connect(lambda value: self.doublespin_funcion(value))

# --- MÉTODOS COMUNES ---
doublespin.setValue(99.99)                  # Establece valor
doublespin.value()                          # Obtiene valor actual (float)
doublespin.setMinimum(0.0)                  # Valor mínimo
doublespin.minimum()                        # Devuelve mínimo
doublespin.setMaximum(999.99)               # Valor máximo
doublespin.maximum()                        # Devuelve máximo
doublespin.setRange(0.0, 999.99)            # Establece rango
doublespin.setSingleStep(0.01)             # Paso de incremento
doublespin.setDecimals(2)                  # Número de decimales
doublespin.decimals()                       # Devuelve decimales
doublespin.setPrefix("$")                   # Prefijo
doublespin.setSuffix(" €")                 # Sufijo
doublespin.cleanText()                     # Texto sin prefijo/sufijo
doublespin.setReadOnly(True)               # Solo lectura
doublespin.setWrapping(True)               # Vuelve al inicio
doublespin.setButtonSymbols(QDoubleSpinBox.PlusMinus)  # Símbolos
doublespin.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)  # Paso adaptativo
doublespin.setAlignment(Qt.AlignCenter)    # Alineación

# --- SEÑALES ---
# doublespin.valueChanged.connect(lambda value: ...)  # Valor cambió (float)

layout.addWidget(doublespin)


# ============================================================================
# QSLIDER
# ============================================================================
# Template: slider
# ============================================================================
slider = QSlider(Qt.Horizontal)
slider.setFixedSize(QSize(200, 30))
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)
slider.valueChanged.connect(lambda value: self.slider_funcion(value))

# --- MÉTODOS COMUNES ---
slider.setValue(75)                         # Establece valor
slider.value()                              # Obtiene valor actual
slider.setMinimum(0)                         # Valor mínimo
slider.minimum()                           # Devuelve mínimo
slider.setMaximum(100)                      # Valor máximo
slider.maximum()                           # Devuelve máximo
slider.setRange(0, 100)                    # Establece rango
slider.setSingleStep(1)                    # Paso de incremento
slider.setPageStep(10)                      # Paso de página (PageUp/PageDown)
slider.setTickPosition(QSlider.TicksBelow) # Marcas: NoTicks, TicksBothSides, TicksAbove, TicksBelow
slider.setTickInterval(10)                 # Intervalo entre marcas
slider.setTracking(True)                   # Actualiza valor durante drag
slider.hasTracking()                       # Devuelve si hay tracking
slider.setInvertedAppearance(True)         # Invierte dirección
slider.setInvertedControls(True)           # Invierte teclas de control
slider.setOrientation(Qt.Vertical)        # Cambia orientación
slider.setSliderPosition(50)              # Posición sin emitir señal
slider.setEnabled(False)                   # Habilitar/deshabilitar
slider.isEnabled()                         # Devuelve si está habilitado

# --- POSICIONES DE TICKS ---
# QSlider.NoTicks                           # Sin marcas
# QSlider.TicksBothSides                   # Ambos lados
# QSlider.TicksAbove (horizontal)           # Arriba
# QSlider.TicksBelow (horizontal)          # Abajo
# QSlider.TicksLeft (vertical)             # Izquierda
# QSlider.TicksRight (vertical)            # Derecha

# --- SEÑALES ---
# slider.valueChanged.connect(lambda value: ...)   # Valor cambió
# slider.sliderPressed.connect(...)               # Presionó slider
# slider.sliderReleased.connect(...)              # Soltó slider
# slider.sliderMoved.connect(lambda value: ...)   # Moviendo slider

layout.addWidget(slider)


# ============================================================================
# QDIAL
# ============================================================================
# Template: dial
# ============================================================================
dial = QDial()
dial.setFixedSize(QSize(150, 150))
dial.setRange(0, 100)
dial.setValue(0)
dial.setNotchesVisible(True)
dial.valueChanged.connect(lambda value: self.dial_funcion(value))

# --- MÉTODOS COMUNES ---
dial.setValue(50)                           # Establece valor
dial.value()                                # Obtiene valor actual
dial.setMinimum(0)                           # Valor mínimo
dial.minimum()                              # Devuelve mínimo
dial.setMaximum(100)                         # Valor máximo
dial.maximum()                              # Devuelve máximo
dial.setRange(0, 100)                      # Establece rango
dial.setNotchesVisible(True)                # Muestra muescas
dial.setNotchTarget(10)                     # Tamaño entre muescas
dial.notchSize()                           # Devuelve tamaño de muesca
dial.setWrapping(True)                      # Permite valores circulares
dial.setTracking(True)                      # Actualiza durante arrastre
dial.setSliderPosition(50)                 # Posición sin señal
dial.setEnabled(False)                      # Habilitar/deshabilitar

# --- SEÑALES ---
# dial.valueChanged.connect(lambda value: ...)   # Valor cambió
# dial.sliderPressed.connect(...)               # Presionó
# dial.sliderReleased.connect(...)              # Soltó
# dial.sliderMoved.connect(lambda value: ...)   # Moviendo

layout.addWidget(dial)


# ============================================================================
# QLCDNUMBER
# ============================================================================
# Template: lcdnumber
# ============================================================================
lcd = QLCDNumber(5)  # 5 dígitos
lcd.display(12345)
lcd.setSegmentStyle(QLCDNumber.Filled)

# --- MÉTODOS COMUNES ---
lcd.display(999)                           # Muestra número (int, float, str)
lcd.setDigitCount(8)                        # Número de dígitos
lcd.digitCount()                           # Devuelve número de dígitos
lcd.setMode(QLCDNumber.Hex)                # Modo: Hex, Dec, Oct, Bin
lcd.mode()                                 # Devuelve modo actual
lcd.setSegmentStyle(QLCDNumber.Flat)       # Estilo: Outlined, Filled, Flat
lcd.segmentStyle()                         # Devuelve estilo
lcd.setSmallDecimalPoint(True)             # Punto decimal pequeño
lcd.smallDecimalPoint()                    # Devuelve si es pequeño
lcd.checkOverflow(9999.99)                # Devuelve si desborda

# --- SEÑALES ---
# lcd.valueChanged.connect(lambda value: ...)  # Valor cambió

layout.addWidget(lcd)


# ============================================================================
# QPROGRESSBAR
# ============================================================================
# Template: progressbar
# ============================================================================
progress = QProgressBar()
progress.setRange(0, 100)
progress.setValue(50)
progress.setFormat("%p% completado")

# --- MÉTODOS COMUNES ---
progress.setValue(75)                       # Establece valor
progress.value()                           # Obtiene valor actual (0-100)
progress.setMinimum(0)                      # Valor mínimo
progress.minimum()                         # Devuelve mínimo
progress.setMaximum(100)                    # Valor máximo
progress.maximum()                         # Devuelve máximo
progress.setRange(0, 100)                  # Establece rango
progress.reset()                           # Reinicia a mínimo
progress.setOrientation(Qt.Horizontal)     # Orientación: Horizontal, Vertical
progress.setTextVisible(True)              # Muestra porcentaje de texto
progress.setFormat("%p%")                   # Formato: %p% = porcentaje, %v = valor, %m = máximo
progress.format()                          # Devuelve formato actual
progress.setAlignment(Qt.AlignCenter)      # Alineación del texto
progress.setInvertedAppearance(True)       # Invierte dirección de progreso

# --- FORMATOS COMUNES ---
# progress.setFormat("%p%")                # "50%"
# progress.setFormat("%p% - %v/%m")        # "50% - 50/100"
# progress.setFormat("%v")                 # "50"

# --- SEÑALES ---
# progress.valueChanged.connect(lambda value: ...)  # Valor cambió

layout.addWidget(progress)


# ============================================================================
# QDATEEDIT
# ============================================================================
# Template: dateedit
# ============================================================================
dateedit = QDateEdit()
dateedit.setDate(QDate.currentDate())
dateedit.setCalendarPopup(True)
dateedit.setDisplayFormat("dd/MM/yyyy")
dateedit.dateChanged.connect(lambda date: self.date_funcion(date))

# --- MÉTODOS COMUNES ---
dateedit.setDate(QDate(2024, 1, 15))       # Establece fecha
dateedit.date()                            # Obtiene fecha (QDate)
dateedit.setMinimumDate(QDate(2020, 1, 1)) # Fecha mínima
dateedit.minimumDate()                     # Devuelve fecha mínima
dateedit.setMaximumDate(QDate(2030, 12, 31))  # Fecha máxima
dateedit.maximumDate()                     # Devuelve fecha máxima
dateedit.setDateRange(QDate(2020, 1, 1), QDate(2030, 12, 31))  # Rango de fechas
dateedit.setCalendarPopup(True)           # Muestra calendario popup
dateedit.calendarPopup()                  # Devuelve si hay popup
dateedit.setDisplayFormat("dd/MM/yyyy")   # Formato: "yyyy-MM-dd", "dd/MM/yyyy"
dateedit.displayFormat()                  # Devuelve formato
dateedit.setEnabled(False)                 # Habilitar/deshabilitar

# --- SEÑALES ---
# dateedit.dateChanged.connect(lambda date: ...)    # Fecha cambió (QDate)
# dateedit.dateTimeChanged.connect(...)             # Fecha/hora cambió

layout.addWidget(dateedit)


# ============================================================================
# QTIMEEDIT
# ============================================================================
# Template: timeedit
# ============================================================================
timeedit = QTimeEdit()
timeedit.setTime(QTime.currentTime())
timeedit.setDisplayFormat("HH:mm:ss")
timeedit.timeChanged.connect(lambda time: self.time_funcion(time))

# --- MÉTODOS COMUNES ---
timeedit.setTime(QTime(14, 30, 0))        # Establece hora
timeedit.time()                            # Obtiene hora (QTime)
timeedit.setMinimumTime(QTime(8, 0))      # Hora mínima
timeedit.minimumTime()                    # Devuelve hora mínima
timeedit.setMaximumTime(QTime(20, 0))     # Hora máxima
timeedit.maximumTime()                    # Devuelve hora máxima
timeedit.setTimeRange(QTime(8, 0), QTime(20, 0))  # Rango de horas
timeedit.setDisplayFormat("HH:mm:ss")     # Formato: "HH:mm", "hh:mm:ss AP"
timeedit.displayFormat()                  # Devuelve formato
timeedit.setEnabled(False)                # Habilitar/deshabilitar

# --- SEÑALES ---
# timeedit.timeChanged.connect(lambda time: ...)  # Hora cambió (QTime)

layout.addWidget(timeedit)


# ============================================================================
# QDATETIMEEDIT
# ============================================================================
# Template: datetimeedit
# ============================================================================
datetimeedit = QDateTimeEdit()
datetimeedit.setDateTime(QDateTime.currentDateTime())
datetimeedit.setDisplayFormat("dd/MM/yyyy HH:mm")
datetimeedit.dateTimeChanged.connect(lambda dt: self.datetime_funcion(dt))

# --- MÉTODOS COMUNES ---
datetimeedit.setDateTime(QDateTime.currentDateTime())  # Establece fecha y hora
datetimeedit.dateTime()                               # Obtiene QDateTime
datetimeedit.setDate(QDate(2024, 1, 15))              # Establece solo fecha
datetimeedit.setTime(QTime(14, 30))                   # Establece solo hora
datetimeedit.date()                                   # Obtiene QDate
datetimeedit.time()                                   # Obtiene QTime
datetimeedit.setMinimumDateTime(QDateTime(2020, 1, 1, 0, 0))  # Mínima
datetimeedit.setMaximumDateTime(QDateTime(2030, 12, 31, 23, 59))  # Máxima
datetimeedit.setCalendarPopup(True)                  # Popup de calendario
datetimeedit.setDisplayFormat("dd/MM/yyyy HH:mm")    # Formato

# --- SEÑALES ---
# datetimeedit.dateTimeChanged.connect(lambda dt: ...)  # Fecha/hora cambió
# datetimeedit.dateChanged.connect(lambda date: ...)    # Fecha cambió
# datetimeedit.timeChanged.connect(lambda time: ...)    # Hora cambió

layout.addWidget(datetimeedit)


# ============================================================================
# QLISTWIDGET
# ============================================================================
# Template: listwidget
# ============================================================================
listwidget = QListWidget()
listwidget.addItems(["Item 1", "Item 2", "Item 3"])
listwidget.itemClicked.connect(lambda item: self.listitem_funcion(item.text()))

# --- MÉTODOS COMUNES ---
listwidget.addItem("Nuevo item")          # Añade un item
listwidget.addItems(["Item A", "Item B"]) # Añade varios items
listwidget.insertItem(0, "Insertar")      # Inserta en posición
listwidget.takeItem(0)                    # Elimina y devuelve item
listwidget.clear()                        # Elimina todos los items
listwidget.currentItem()                  # Item actual
listwidget.currentRow()                   # Fila actual
listwidget.setCurrentRow(0)               # Selecciona fila
listwidget.setCurrentItem(item)          # Selecciona item
listwidget.row(item)                     # Devuelve fila de item
listwidget.count()                        # Número de items
listwidget.item(0)                        # Item en fila
listwidget.selectedItems()               # Lista de items seleccionados
listwidget.setSelectionMode(QListWidget.MultiSelection)  # Modo: SingleSelection, ContiguousSelection, MultiSelection, ExtendedSelection, NoSelection
listwidget.setDragDropMode(QListWidget.DragDrop)  # Modo drag & drop
listwidget.sortItems(Qt.AscendingOrder)  # Ordena
listwidget.isSortingEnabled()            # Devuelve si hay ordenación
listwidget.setSortingEnabled(True)       # Habilita ordenación

# --- MODIFICAR ITEMS ---
item = listwidget.item(0)
item.setText("Nuevo texto")              # Cambia texto
item.text()                              # Obtiene texto
item.setIcon(QIcon("icon.png"))          # Establece icono
item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)  # Flags
item.setCheckState(Qt.Checked)          # Con checkbox
item.setData(Qt.UserRole, "dato")       # Dato personalizado
item.data(Qt.UserRole)                  # Obtiene dato

# --- SEÑALES ---
# listwidget.currentItemChanged.connect(lambda current, previous: ...)
# listwidget.currentRowChanged.connect(lambda row: ...)
# listwidget.itemClicked.connect(lambda item: ...)
# listwidget.itemDoubleClicked.connect(lambda item: ...)
# listwidget.itemSelectionChanged.connect(...)
# listwidget.itemChanged.connect(lambda item: ...)

layout.addWidget(listwidget)


# ============================================================================
# QTABLEVIEW
# ============================================================================
# Template: tableview
# ============================================================================
table = QTableView()
model = QStandardItemModel(0, 3)  # 0 filas, 3 columnas
model.setHorizontalHeaderLabels(["Col 1", "Col 2", "Col 3"])
table.setModel(model)
table.setEditTriggers(QTableView.NoEditTriggers)

# --- MÉTODOS COMUNES ---
table.setModel(model)                   # Establece modelo
table.model()                           # Devuelve modelo
table.setSelectionModel(selection)       # Modelo de selección
table.setSelectionBehavior(QTableView.SelectRows)  # Comportamiento: SelectRows, SelectColumns, SelectItems
table.setSelectionMode(QTableView.SingleSelection)  # Modo: SingleSelection, ContiguousSelection, MultiSelection, ExtendedSelection, NoSelection
table.setEditTriggers(QTableView.NoEditTriggers)  # Disparadores: NoEditTriggers, CurrentChanged, DoubleClicked, SelectedClicked, EditKeyPressed, AnyKeyPressed, AllEditTriggers
table.selectedIndexes()                # Lista de índices seleccionados
table.currentIndex()                    # Índice actual
table.clearSelection()                  # Limpia selección
table.selectAll()                       # Selecciona todo

# --- COLUMNAS Y FILAS ---
table.setColumnWidth(0, 100)            # Ancho de columna
table.setRowHeight(0, 30)              # Alto de fila
table.resizeColumnToContents(0)        # Ajusta columna al contenido
table.resizeRowToContents(0)            # Ajusta fila al contenido
table.resizeColumnsToContents()        # Ajusta todas las columnas
table.setColumnHidden(0, True)         # Oculta/mostra columna
table.setRowHidden(0, True)            # Oculta/mostra fila
table.sortByColumn(0, Qt.AscendingOrder)  # Ordena por columna
table.setSortingEnabled(True)          # Habilita ordenación

# --- CABECERA ---
table.verticalHeader().setVisible(False)  # Oculta cabecera vertical
table.horizontalHeader().setStretchLastSection(True)  # Estira última columna
table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Modo resize

# --- AÑADIR DATOS AL MODELO ---
item = QStandardItem("Dato")
item.setTextAlignment(Qt.AlignCenter)
item.setEditable(False)
item.setBackground(QColor("lightblue"))
item.setForeground(QColor("darkblue"))
item.setFont(QFont("Arial", 10, QFont.Bold))
model.setItem(fila, columna, item)     # Establece item
model.appendRow([item1, item2, item3]) # Añade fila
model.insertRow(0)                      # Inserta fila
model.removeRow(0)                      # Elimina fila
model.setRowCount(0)                    # Limpia todas las filas

# --- SEÑALES ---
# table.clicked.connect(lambda index: ...)
# table.doubleClicked.connect(lambda index: ...)
# table.activated.connect(lambda index: ...)
# table.entered.connect(lambda index: ...)
# table.selectionModel().selectionChanged.connect(...)

layout.addWidget(table)


# ============================================================================
# QTABWIDGET
# ============================================================================
# Template: tabwidget
# ============================================================================
tabwidget = QTabWidget()
tabwidget.setTabPosition(QTabWidget.North)  # North, South, West, East
tabwidget.setMovable(True)

# --- MÉTODOS COMUNES ---
tabwidget.addTab(page, "Pestaña 1")      # Añade pestaña
tabwidget.addTab(page, QIcon("icon.png"), "Con icono")  # Con icono
tabwidget.insertTab(0, page, "Nueva")    # Inserta pestaña
tabwidget.removeTab(0)                  # Elimina pestaña
tabwidget.clear()                       # Elimina todas las pestañas
tabwidget.setTabText(0, "Nuevo nombre") # Establece texto de pestaña
tabwidget.tabText(0)                   # Devuelve texto de pestaña
tabwidget.setTabIcon(0, QIcon("i.png")) # Establece icono
tabwidget.tabIcon(0)                   # Devuelve icono
tabwidget.setTabToolTip(0, "Tooltip")  # Tooltip de pestaña
tabwidget.setTabEnabled(0, False)      # Habilita/deshabilita pestaña
tabwidget.isTabEnabled(0)              # Devuelve si está habilitada
tabwidget.setTabVisible(0, False)      # Muestra/oculta pestaña
tabwidget.setCurrentIndex(0)           # Establece pestaña activa
tabwidget.currentIndex()               # Devuelve índice actual
tabwidget.currentWidget()              # Devuelve widget actual
tabwidget.widget(0)                     # Devuelve widget de índice
tabwidget.indexOf(widget)              # Devuelve índice de widget
tabwidget.count()                       # Número de pestañas
tabwidget.setTabPosition(QTabWidget.West)  # Posición: North, South, West, East
tabwidget.setTabShape(QTabWidget.Rounded)  # Forma: Rounded, Triangular
tabwidget.setDocumentMode(True)        # Modo documento (sin marco)
tabwidget.setMovable(True)             # Pestañas movibles
tabwidget.setUsesScrollButtons(True)   # Botones de scroll
tabwidget.setIconSize(QSize(16, 16))   # Tamaño de icono

# --- AÑADIR CONTENIDO A PESTAÑAS ---
page1 = QWidget()
page1_layout = QVBoxLayout()
page1_layout.addWidget(QLabel("Contenido 1"))
page1.setLayout(page1_layout)
tabwidget.addTab(page1, "Pestaña 1")

# --- CON CUSTOMCOLORLABEL ---
for n, color in enumerate(["red", "green", "blue"]):
    tabwidget.addTab(CustomColorLabel(color, f"Tab {n}"), color)

# --- SEÑALES ---
# tabwidget.currentChanged.connect(lambda index: ...)     # Índice cambió
# tabwidget.tabCloseRequested.connect(lambda index: ...)   # Pide cerrar pestaña
# tabwidget.tabMoved.connect(lambda from_idx, to_idx: ...) # Pestaña movida

layout.addWidget(tabwidget)


# ============================================================================
# QMENU Y QACTION (MENÚ)
# ============================================================================
# Template: menu
# ============================================================================
menu_bar = self.menuBar()
file_menu = menu_bar.addMenu("&Fichero")  # & crea atajo Alt+F
file_menu.setStatusTip("Menú de ficheros")

# --- MÉTODOS QACTION ---
action = QAction(QIcon("icons/icons/icon.png"), "&Abrir", self)
action.setText("Nuevo texto")             # Establece texto
action.text()                              # Devuelve texto
action.setIcon(QIcon("icon.png"))         # Establece icono
action.icon()                              # Devuelve icono
action.setShortcut(QKeySequence("Ctrl+O"))  # Atajo de teclado
action.shortcut()                          # Devuelve atajo
action.setStatusTip("Tooltip de estado")  # Tooltip barra de estado
action.statusTip()                        # Devuelve tooltip
action.setToolTip("Tooltip")              # Tooltip
action.setData("dato")                    # Dato asociado
action.data()                             # Devuelve dato
action.setCheckable(True)                 # Marcable
action.setChecked(True)                   # Marcado
action.isChecked()                        # Devuelve si está marcado
action.setEnabled(False)                  # Habilitado/deshabilitado
action.isEnabled()                        # Devuelve si está habilitado
action.setVisible(False)                  # Visible/oculto
action.setIconVisibleInMenu(True)         # Icono visible en menú
action.setShortcutContext(Qt.WindowShortcut)  # Contexto: WidgetWithChildrenShortcut, WindowShortcut, ApplicationShortcut

# --- AÑADIR AL MENÚ ---
file_menu.addAction(action)               # Añade acción
file_menu.addSeparator()                 # Separador
file_menu.addMenu("Submenú")            # Crea submenú

# --- SEÑALES ---
# action.triggered.connect(...)           # Acción activada
# action.toggled.connect(lambda checked: ...)  # Si es checkable

# ============================================================================
# QTOOLBAR
# ============================================================================
# Template: toolbar
# ============================================================================
toolbar = QToolBar("Toolbar")
toolbar.setIconSize(QSize(32, 32))
toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
toolbar.addAction(action)
self.addToolBar(toolbar)

# --- MÉTODOS COMUNES ---
toolbar.addAction(action)                # Añade acción
toolbar.addActions([action1, action2])  # Añade varias
toolbar.addSeparator()                  # Separador
toolbar.addWidget(widget)               # Añade widget
toolbar.addBreak()                      # Nueva línea
toolbar.removeAction(action)           # Elimina acción
toolbar.clear()                         # Limpia todo
toolbar.setMovable(True)               # Movible
toolbar.isMovable()                    # Devuelve si es movible
toolbar.setFloatable(True)             # Flotante
toolbar.isFloatable()                  # Devuelve si flota
toolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)  # Áreas permitidas
toolbar.setIconSize(QSize(24, 24))     # Tamaño de icono
toolbar.toggleViewAction()             # Acción para mostrar/ocultar

# --- SEÑALES ---
# toolbar.actionTriggered.connect(lambda action: ...)

# ============================================================================
# QSTATUSBAR
# ============================================================================
# Template: statusbar
# ============================================================================
statusbar = QStatusBar(self)
self.setStatusBar(statusbar)

# --- MÉTODOS COMUNES ---
statusbar.showMessage("Listo", 3000)    # Mensaje temporal (ms), 0 = permanente
statusbar.clearMessage()               # Limpia mensaje actual
statusbar.addWidget(QLabel("Widget"))   # Añade widget permanente
statusbar.addPermanentWidget(QLabel("PP"))  # Widget no temporal
statusbar.removeWidget(widget)          # Elimina widget
statusbar.setSizeGripEnabled(False)    # Grip de redimensión

# --- SEÑALES ---
# statusbar.messageChanged.connect(lambda text: ...)


# ============================================================================
# QMESSAGEBOX
# ============================================================================
# Template: messagebox
# ============================================================================

# --- MÉTODOS COMUNES (INSTANCIA) ---
dialog = QMessageBox(self)
dialog.setWindowTitle("Título")
dialog.setText("Mensaje principal")
dialog.setInformativeText("Información adicional")
dialog.setDetailedText("Detalles expandibles")
dialog.setIcon(QMessageBox.Information)  # NoIcon, Information, Warning, Critical, Question
dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
dialog.setDefaultButton(QMessageBox.Ok)
dialog.setEscapeButton(QMessageBox.Cancel)
button = dialog.exec()  # Muestra y devuelve botón presionado

# --- BOTONES ---
# QMessageBox.Ok, Cancel, Yes, No, YesToAll, NoToAll, Abort, Retry, Ignore, Close, NoButton
# Combinar: QMessageBox.Yes | QMessageBox.No

# --- MÉTODOS ESTÁTICOS (FÁCILES) ---
QMessageBox.information(self, "Título", "Mensaje", QMessageBox.Ok)
QMessageBox.warning(self, "Título", "Mensaje", QMessageBox.Ok)
QMessageBox.critical(self, "Título", "Mensaje", QMessageBox.Ok)
QMessageBox.question(self, "Título", "¿Pregunta?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
QMessageBox.about(self, "Acerca de", "Mi aplicación")
QMessageBox.aboutQt(self, "Acerca de Qt")

# --- ICONOS ---
# QMessageBox.NoIcon
# QMessageBox.Information (azul i)
# QMessageBox.Warning (amarillo !)
# QMessageBox.Critical (rojo X)
# QMessageBox.Question (azul ?)

# --- EJEMPLO PRÁCTICO ---
button = QMessageBox.question(
    self,
    "Confirmar",
    "¿Desea guardar los cambios?",
    QMessageBox.Yes | QMessageBox.No,
    QMessageBox.No
)
if button == QMessageBox.Yes:
    # Guardar
    pass
elif button == QMessageBox.No:
    # No guardar
    pass


# ============================================================================
# QFILEDIALOG
# ============================================================================
# Template: filedialog
# ============================================================================

# --- ABRIR ARCHIVO ---
filename, filter = QFileDialog.getOpenFileName(
    self,
    "Abrir archivo",
    "/home",
    "Archivos texto (*.txt);;Todos (*.*);;PDF (*.pdf)"
)
if filename:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

# --- ABRIR VARIOS ARCHIVOS ---
filenames, filter = QFileDialog.getOpenFileNames(
    self,
    "Abrir archivos",
    "/home",
    "Archivos texto (*.txt)"
)
for f in filenames:
    print(f)

# --- GUARDAR ARCHIVO ---
filename, filter = QFileDialog.getSaveFileName(
    self,
    "Guardar archivo",
    "",
    "Archivos texto (*.txt)"
)
if filename:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("contenido")

# --- SELECCIONAR DIRECTORIO ---
directory = QFileDialog.getExistingDirectory(self, "Seleccionar directorio")

# --- CONFIGURACIÓN DE DIÁLOGO ---
dialog = QFileDialog(self)
dialog.setWindowTitle("Mi diálogo")
dialog.setDirectory("/home")
dialog.setNameFilter("Archivos (*.*)")
dialog.setFileMode(QFileDialog.ExistingFiles)  # AnyFile, ExistingFile, Directory, ExistingFiles, DirectoryOnly
dialog.setAcceptMode(QFileDialog.AcceptOpen)   # AcceptOpen, AcceptSave
dialog.setOption(QFileDialog.HideNameFilterDetails)  # Oculta detalles del filtro

if dialog.exec():
    files = dialog.selectedFiles()  # Lista de archivos seleccionados


# ============================================================================
# QDIALOG (DIÁLOGO PERSONALIZADO)
# ============================================================================
# Template: dialog
# ============================================================================
dialog = QDialog(self)
dialog.setModal(True)
dialog.setWindowTitle("Mi Diálogo")
dialog.setFixedSize(300, 200)

# --- MÉTODOS COMUNES ---
dialog.setModal(True)                    # Modal (bloquea padre)
dialog.isModal()                         # Devuelve si es modal
dialog.accept()                          # Acepta y cierra (result = Accepted)
dialog.reject()                          # Rechaza y cierra (result = Rejected)
dialog.done(0)                           # Cierra con código
dialog.exec()                            # Muestra modal (bloqueante)
dialog.open()                            # Muestra no modal
dialog.result()                          # Código de resultado (Accepted=1, Rejected=0)

# --- CONTENIDO ---
dialog_layout = QVBoxLayout()
dialog_layout.addWidget(QLabel("Contenido"))
dialog.setLayout(dialog_layout)

if dialog.exec() == QDialog.Accepted:
    print("Diálogo aceptado")
else:
    print("Diálogo rechazado")


# ============================================================================
# QGRIDLAYOUT
# ============================================================================
# Template: gridlayout
# ============================================================================
grid = QGridLayout()

# --- MÉTODOS COMUNES ---
grid.addWidget(widget, fila, columna)                    # Añade widget
grid.addWidget(widget, 0, 0, 1, 2)                        # Ocupa: fila, col, rowSpan, colSpan
grid.addLayout(sublayout, 1, 0)                          # Añade sub-layout
grid.setRowStretch(fila, peso)                           # Estiramiento de fila
grid.setColumnStretch(columna, peso)                     # Estiramiento de columna
grid.setRowMinimumHeight(fila, altura)                    # Altura mínima de fila
grid.setColumnMinimumWidth(columna, ancho)                # Ancho mínimo de columna
grid.setSpacing(10)                                       # Espaciado entre celdas
grid.setHorizontalSpacing(5)                              # Espaciado horizontal
grid.setVerticalSpacing(10)                              # Espaciado vertical
grid.itemAtPosition(fila, columna)                       # Item en posición
grid.getItemPosition(index)                              # Posición de item (row, col, rowSpan, colSpan)
grid.removeWidget(widget)                                # Elimina widget
grid.count()                                             # Número de items
grid.itemAt(index)                                       # Item en índice


# ============================================================================
# QVBOXLAYOUT / QHBOXLAYOUT
# ============================================================================
# Template: boxlayout
# ============================================================================
layout_v = QVBoxLayout()
layout_h = QHBoxLayout()

# --- MÉTODOS COMUNES ---
layout_v.addWidget(widget)                               # Añade widget
layout_v.addLayout(sublayout)                            # Añade sub-layout
layout_v.addStrut(50)                                    # Espaciador rígido
layout_v.addSpacing(10)                                  # Espacio entre widgets
layout_v.addStretch(peso)                                # Espaciador elástico
layout_v.insertWidget(index, widget)                     # Inserta widget
layout_v.insertLayout(index, layout)                     # Inserta layout
layout_v.insertSpacing(index, size)                      # Inserta espacio
layout_v.insertStretch(index, stretch)                   # Inserta stretch
layout_v.removeWidget(widget)                           # Elimina widget
layout_v.count()                                         # Número de items
layout_v.setSpacing(10)                                  # Espaciado entre widgets
layout_v.setContentsMargins(10, 10, 10, 10)              # Márgenes: left, top, right, bottom
layout_v.setStretchFactor(widget, 1)                     # Factor de estiramiento


# ============================================================================
# QMAINWINDOW (ESTRUCTURA COMPLETA)
# ============================================================================
# Template: mainwindow
# ============================================================================
"""
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QComboBox,
    QSpinBox, QDoubleSpinBox, QSlider, QDial, QStatusBar, QToolBar, QAction,
    QMessageBox, QFileDialog, QDialog, QTabWidget, QTableView, QStandardItemModel, QStandardItem
)

FONT_SIZE = 15

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(800, 600)

        # StatusBar
        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

        # Layout principal
        layout = QVBoxLayout()

        # TU CÓDIGO AQUÍ

        # Widget contenedor
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_widget_font(self, widget, font_size):
        font = widget.font()
        font.setPointSize(font_size)
        widget.setFont(font)

    # === TUS MÉTODOS AQUÍ ===

# Punto de entrada
app = QApplication(sys.argv)
window = MainWindow("Mi App")
window.show()
app.exec()
"""


# ============================================================================
# EJEMPLO PRÁCTICO: FORMULARIO COMPLETO
# ============================================================================

def ejemplo_formulario():
    """
    Ejemplo completo de formulario con múltiples widgets.
    """

    # --- LAYOUTS ---
    layout_main = QVBoxLayout()
    layout_form = QGridLayout()
    layout_buttons = QHBoxLayout()

    # --- CAMPOS DEL FORMULARIO ---
    # Nombre
    lbl_nombre = QLabel("Nombre:")
    line_nombre = QLineEdit()
    line_nombre.setPlaceholderText("Escribe tu nombre")

    # Email
    lbl_email = QLabel("Email:")
    line_email = QLineEdit()
    line_email.setPlaceholderText("tu@email.com")

    # Edad
    lbl_edad = QLabel("Edad:")
    spin_edad = QSpinBox()
    spin_edad.setRange(0, 120)
    spin_edad.setValue(18)

    # Género
    lbl_genero = QLabel("Género:")
    combo_genero = QComboBox()
    combo_genero.addItems(["Masculino", "Femenino", "Otro"])

    # Aceptar términos
    check_terminos = QCheckBox("Acepto los términos y condiciones")

    # Botones
    btn_guardar = QPushButton("Guardar")
    btn_cancelar = QPushButton("Cancelar")

    # --- AÑADIR AL GRID ---
    layout_form.addWidget(lbl_nombre, 0, 0)
    layout_form.addWidget(line_nombre, 0, 1)
    layout_form.addWidget(lbl_email, 1, 0)
    layout_form.addWidget(line_email, 1, 1)
    layout_form.addWidget(lbl_edad, 2, 0)
    layout_form.addWidget(spin_edad, 2, 1)
    layout_form.addWidget(lbl_genero, 3, 0)
    layout_form.addWidget(combo_genero, 3, 1)
    layout_form.addWidget(check_terminos, 4, 0, 1, 2)

    # --- AÑADIR BOTONES ---
    layout_buttons.addStretch()
    layout_buttons.addWidget(btn_guardar)
    layout_buttons.addWidget(btn_cancelar)

    # --- ENSAMBLAR ---
    layout_main.addLayout(layout_form)
    layout_main.addLayout(layout_buttons)

    return {
        "nombre": line_nombre,
        "email": line_email,
        "edad": spin_edad,
        "genero": combo_genero,
        "terminos": check_terminos,
        "guardar": btn_guardar,
        "cancelar": btn_cancelar
    }