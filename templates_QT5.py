# ============================================================================
# PLANTILLAS QT5 - TODOS LOS WIDGETS Y MÉTODOS
# ============================================================================

"""
Este archivo contiene plantillas de todos los widgets de PyQt5 usados
en el proyecto, con sus métodos principales y explicaciones.
"""

import sys

from PyQt5.QtCore import Qt, QSize, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QColor, QFont, QKeySequence, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit,
    QCheckBox, QRadioButton, QComboBox, QSpinBox, QDoubleSpinBox,
    QSlider, QDial, QLCDNumber, QProgressBar,
    QDateEdit, QTimeEdit, QDateTimeEdit, QFontComboBox,
    QMenu, QAction, QStatusBar, QToolBar, QMenuBar,
    QMessageBox, QFileDialog, QDialog,
    QListWidget, QTableView, QListView,
    QTabWidget
)

# ============================================================================
# APLICACIÓN Y VENTANA PRINCIPAL
# ============================================================================

# -------------------------------------------------------------------
# QApplication - Punto de entrada de toda aplicación Qt
# -------------------------------------------------------------------
"""
app = QApplication(sys.argv)
# Argumentos:
#   - sys.argv: argumentos de línea de comandos para Qt
#
# Métodos principales:
#   exec()        -> Inicia el event loop de la aplicación (BUCLE INFINITO)
#   quit()        -> Cierra la aplicación
#   setStyle(s)   -> Establece el estilo visual ("Fusion", "Windows", etc.)
"""
app = QApplication(sys.argv)

# -------------------------------------------------------------------
# QMainWindow - Ventana principal con barra de menú y estado
# -------------------------------------------------------------------
"""
window = QMainWindow(parent=None)
# Hereda de QWidget, añade funcionalidad de barra de menú y barras de herramientas
#
# Métodos principales:
#   setWindowTitle(title)       -> Establece el título de la ventana
#   setWindowIcon(icon)         -> Establece el icono de la ventana
#   setCentralWidget(widget)    -> Establece el widget central
#   setFixedSize(w, h)          -> Fija el tamaño de la ventana
#   setGeometry(x, y, w, h)     -> Establece posición y tamaño
#   menuBar()                    -> Devuelve la barra de menú (crea si no existe)
#   addToolBar(toolbar)          -> Añade una barra de herramientas
#   setStatusBar(statusbar)      -> Establece la barra de estado
#   statusBar()                  -> Devuelve la barra de estado
#   setStatusTip(text)           -> Establece tooltip para la ventana
#
# Señales:
#   windowTitleChanged(str)      -> Se emite cuando cambia el título
"""
window = QMainWindow()

# ============================================================================
# WIDGETS DE BOTONES
# ============================================================================

# -------------------------------------------------------------------
# QPushButton - Botón clickeable
# -------------------------------------------------------------------
"""
button = QPushButton(text="Click me", parent=None)
#
# Constructor:
#   - text: texto del botón
#   - parent: widget padre
#
# Métodos principales:
#   setText(text)                -> Establece el texto del botón
#   text()                       -> Devuelve el texto
#   setIcon(icon)               -> Establece un icono
#   setIconSize(size)           -> Establece el tamaño del icono
#   setFlat(bool)               -> Botón plano (sin borde)
#   setDefault(bool)            -> Botón por defecto (Enter)
#   setAutoDefault(bool)        -> Auto-default en diálogos
#   setCheckable(bool)          -> Puede estar marcado/no marcado (toggle)
#   setChecked(bool)            -> Establece estado checked
#   isChecked()                 -> Devuelve si está marcado
#   setEnabled(bool)            -> Habilita/deshabilita el botón
#   isEnabled()                 -> Devuelve si está habilitado
#   animateClick(ms)            -> Simula click con animación
#   click()                      -> Simula un click
#   setShortcut(keysequence)    -> Asigna atajo de teclado
#   setToolTip(text)            -> Tooltip al pasar el ratón
#
# Señales:
#   clicked(bool checked=False) -> Se emite al hacer click
#   pressed()                   -> Se emite al presionar
#   released()                  -> Se emite al soltar
#   toggled(bool checked)       -> Se emite al cambiar estado (checkable)
"""
button = QPushButton("Click me")

# Ejemplo con conexión
button.clicked.connect(lambda: print("Click!"))

# -------------------------------------------------------------------
# QCheckBox - Casilla de verificación (puede estar marcada)
# -------------------------------------------------------------------
"""
checkbox = QCheckBox(text="Aceptar términos", parent=None)
#
# Constructor:
#   - text: texto de la etiqueta
#   - parent: widget padre
#
# Métodos principales:
#   setText(text)                -> Establece el texto
#   text()                       -> Devuelve el texto
#   setChecked(bool)            -> Marca/desmarca
#   isChecked()                 -> Devuelve si está marcado
#   setTristate(bool)           -> Tres estados: marcado, desmarcado, parcial
#   setCheckState(state)        -> Establece estado (Qt.Unchecked, Qt.PartiallyChecked, Qt.Checked)
#   checkState()                -> Devuelve estado actual
#
# Señales:
#   stateChanged(int state)     -> Se emite cuando cambia el estado
"""
checkbox = QCheckBox("Aceptar")
checkbox.stateChanged.connect(lambda state: print(f"Estado: {state}"))

# -------------------------------------------------------------------
# QRadioButton - Botón de radio (selección única en grupo)
# -------------------------------------------------------------------
"""
radio = QRadioButton(text="Opción 1", parent=None)
#
# Constructor:
#   - text: texto de la etiqueta
#   - parent: widget padre
#
# Métodos principales:
#   setText(text)                -> Establece el texto
#   text()                       -> Devuelve el texto
#   setChecked(bool)            -> Selecciona el radio
#   isChecked()                 -> Devuelve si está seleccionado
#   setAutoExclusive(bool)      -> Exclusividad automática (por defecto True)
#
# Señales:
#   clicked(bool checked)       -> Se emite al hacer click
#   toggled(bool checked)       -> Se emite al cambiar selección
"""
radio1 = QRadioButton("Opción 1")
radio2 = QRadioButton("Opción 2")

# ============================================================================
# WIDGETS DE TEXTO
# ============================================================================

# -------------------------------------------------------------------
# QLabel - Etiqueta de texto (solo lectura)
# -------------------------------------------------------------------
"""
label = QLabel(text="", parent=None)
#
# Constructor:
#   - text: texto a mostrar (opcional)
#   - parent: widget padre
#
# Métodos principales:
#   setText(text)                -> Establece el texto
#   text()                       -> Devuelve el texto
#   setAlignment(align)         -> Alineación: Qt.AlignLeft, Center, Right, etc.
#   setPixmap(pixmap)           -> Establece una imagen
#   pixmap()                     -> Devuelve la imagen
#   setWordWrap(bool)           -> Ajuste de línea automático
#   setIndent(pixels)           -> Sangría
#   setMargin(pixels)           -> Margen interno
#   setStyleSheet(css)          -> Estilo CSS
#   setFont(font)               -> Fuente del texto
#   setOpenExternalLinks(bool) -> Abre enlaces externos (HTML)
#   clear()                      -> Limpia el texto
#
# Ejemplos de alineación:
#   Qt.AlignLeft | Qt.AlignVCenter
#   Qt.AlignHCenter | Qt.AlignVCenter
#   Qt.AlignRight
#   Qt.AlignCenter
"""
label = QLabel("Texto")
label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

# -------------------------------------------------------------------
# QLineEdit - Campo de texto de una línea
# -------------------------------------------------------------------
"""
lineedit = QLineEdit(parent=None)
# También: QLineEdit(placeholder_text, parent=None)
#
# Métodos principales:
#   setText(text)                -> Establece el texto
#   text()                       -> Devuelve el texto
#   setPlaceholderText(text)    -> Texto marcador (gris claro)
#   placeholderText()           -> Devuelve el texto marcador
#   setMaxLength(length)        -> Longitud máxima de caracteres
#   maxLength()                 -> Devuelve longitud máxima
#   setReadOnly(bool)           -> Solo lectura
#   isReadOnly()                 -> Devuelve si es solo lectura
#   setEnabled(bool)            -> Habilita/deshabilita
#   setClearButtonEnabled(bool) -> Botón para limpiar
#   selectAll()                 -> Selecciona todo el texto
#   setSelection(start, length) -> Selecciona rango de texto
#   selectedText()             -> Devuelve texto seleccionado
#   setEchoMode(mode)           -> Modo de visualización:
#                                   QLineEdit.Normal
#                                   QLineEdit.Password (********)
#                                   QLineEdit.NoEcho
#                                   QLineEdit.PasswordEchoOnEdit
#   echoMode()                  -> Devuelve modo actual
#   setValidator(validator)     -> Validador (QIntValidator, QDoubleValidator, etc.)
#   setInputMask(mask)         -> Máscara de entrada (ej: "999.999.999.999")
#   setAlignment(align)        -> Alineación del texto
#   setFont(font)               -> Fuente
#   clear()                      -> Limpia el campo
#   copy()                       -> Copia texto seleccionado
#   cut()                        -> Corta texto seleccionado
#   paste()                      -> Pega texto del portapapeles
#   undo()                       -> Deshace última acción
#   redo()                       -> Rehace última acción
#
# Señales:
#   textChanged(str text)       -> Se emite cuando cambia el texto
#   textEdited(str text)        -> Se emite al editar (no en setText)
#   editingFinished()           -> Se emite al terminar edición (Enter o Tab)
#   returnPressed()             -> Se emite al presionar Enter
#   selectionChanged()          -> Se emite al cambiar selección
"""
lineedit = QLineEdit()
lineedit.setPlaceholderText("Escribe aquí...")
lineedit.textChanged.connect(lambda text: print(f"Texto: {text}"))

# -------------------------------------------------------------------
# QTextEdit - Editor de texto multilínea
# -------------------------------------------------------------------
"""
textedit = QTextEdit(parent=None)
# También: QTextEdit(html, parent=None)
#
# Métodos principales:
#   setText(text)                -> Establece texto plano
#   toPlainText()               -> Devuelve texto plano (sin HTML)
#   setHtml(html)               -> Establece contenido HTML
#   toHtml()                    -> Devuelve contenido HTML
#   setMarkdown(md)             -> Establece contenido Markdown
#   toMarkdown()                -> Devuelve como Markdown
#   setPlainText(text)          -> Establece texto plano
#   append(text)                -> Añade texto al final (nueva línea)
#   clear()                      -> Limpia el contenido
#   setReadOnly(bool)           -> Solo lectura
#   setEnabled(bool)            -> Habilita/deshabilita
#   setFont(font)               -> Fuente
#   setTextColor(color)         -> Color del texto
#   setTextBackgroundColor(color) -> Color de fondo del texto
#   setAlignment(align)         -> Alineación del texto
#   setLineWrapMode(mode)       -> Modo de ajuste de línea:
#                                   QTextEdit.NoWrap
#                                   QTextEdit.WidgetWidth
#                                   QTextEdit.FixedPixelWidth
#                                   QTextEdit.FixedColumnWidth
#   setLineWrapColumnOrWidth(pixels) -> Ancho de columnas para wrap
#   setTabChangesFocus(bool)    -> Tab cambia foco (no inserta tab)
#   setAcceptRichText(bool)     -> Acepta texto enriquecido
#   setPlaceholderText(text)    -> Texto marcador (Qt5.2+)
#   print_(printer)             -> Imprime contenido
#
# Formato de texto (usando QTextCursor):
#   setFontWeight(weight)       -> Peso de fuente (QFont.Bold, etc.)
#   setFontUnderline(bool)      -> Subrayado
#   setFontItalic(bool)         -> Cursiva
#   insertPlainText(text)       -> Inserta texto plano
#   insertHtml(html)            -> Inserta HTML
#
# Señales:
#   textChanged()                -> Se emite cuando cambia contenido
#   copyAvailable(bool)         -> Se emite cuando hay texto disponible para copiar
#   selectionChanged()           -> Se emite al cambiar selección
#   currentCharFormatChanged(QTextCharFormat) -> Formato cambiado
#   redoAvailable(bool)         -> Rehacer disponible
#   undoAvailable(bool)         -> Deshacer disponible
#   cursorPositionChanged()      -> Posición del cursor cambió
"""
textedit = QTextEdit()
textedit.setText("Contenido inicial")
textedit.textChanged.connect(lambda: print("Texto cambió"))
content = textedit.toPlainText()

# ============================================================================
# WIDGETS DE SELECCIÓN NUMÉRICA
# ============================================================================

# -------------------------------------------------------------------
# QSpinBox - Selector de números enteros
# -------------------------------------------------------------------
"""
spinbox = QSpinBox(parent=None)
#
# Métodos principales:
#   setValue(val)               -> Establece valor
#   value()                     -> Devuelve valor actual
#   setMinimum(val)             -> Valor mínimo
#   minimum()                    -> Devuelve mínimo
#   setMaximum(val)             -> Valor máximo
#   maximum()                    -> Devuelve máximo
#   setRange(min, max)          -> Establece rango [min, max]
#   setSingleStep(val)           -> Paso de incremento/decremento
#   singleStep()                 -> Devuelve paso
#   setPrefix(text)             -> Prefijo (ej: "$")
#   prefix()                     -> Devuelve prefijo
#   setSuffix(text)             -> Sufijo (ej: "€", " items")
#   suffix()                     -> Devuelve sufijo
#   setReadOnly(bool)           -> Solo lectura
#   setWrapping(bool)           -> Vuelve al inicio al pasar máximo
#   setButtonSymbols(symbols)   -> Símbolos de botones:
#                                   QSpinBox.UpDownArrows
#                                   QSpinBox.PlusMinus
#   setAlignment(align)         -> Alineación del valor
#   cleanText()                 -> Texto sin prefijo/sufijo
#
# Señales:
#   valueChanged(int value)    -> Se emite cuando cambia valor
#   valueChanged(str value)    -> Sobrecargada con string
#   editingFinished()           -> Se emite al terminar edición
"""
spinbox = QSpinBox()
spinbox.setRange(0, 100)
spinbox.setValue(50)
spinbox.setSuffix(" €")
spinbox.valueChanged.connect(lambda v: print(f"Valor: {v}"))

# -------------------------------------------------------------------
# QDoubleSpinBox - Selector de números decimales
# -------------------------------------------------------------------
"""
doublespinbox = QDoubleSpinBox(parent=None)
#
# Métodos principales:
#   (los mismos que QSpinBox, más:)
#   setDecimals(count)         -> Número de decimales a mostrar
#   decimals()                  -> Devuelve número de decimales
#   setStepType(type)           -> Tipo de paso:
#                                   QAbstractSpinBox.AdaptiveDecimalStepType
#   setString(val)              -> Convierte double a string
#   valueFromText(text)         -> Convierte texto a valor
#
# Señales:
#   valueChanged(double value) -> Se emite cuando cambia valor
"""
doublespinbox = QDoubleSpinBox()
doublespinbox.setRange(0.0, 100.0)
doublespinbox.setValue(25.50)
doublespinbox.setSuffix(" €")
doublespinbox.setDecimals(2)

# -------------------------------------------------------------------
# QSlider - Deslizador horizontal o vertical
# -------------------------------------------------------------------
"""
slider = QSlider(orientation=Qt.Horizontal, parent=None)
# También: QSlider(Qt.Vertical)
#
# Constructor:
#   - orientation: Qt.Horizontal o Qt.Vertical
#
# Métodos principales:
#   setValue(val)               -> Establece valor
#   value()                     -> Devuelve valor actual
#   setMinimum(val)             -> Valor mínimo
#   minimum()                    -> Devuelve mínimo
#   setMaximum(val)             -> Valor máximo
#   maximum()                    -> Devuelve máximo
#   setRange(min, max)          -> Establece rango
#   setSingleStep(val)           -> Paso de incremento
#   singleStep()                 -> Devuelve paso
#   setPageStep(val)             -> Paso de página (Page Up/Down)
#   setTickPosition(position)   -> Posición de marcas:
#                                   QSlider.NoTicks
#                                   QSlider.TicksBothSides
#                                   QSlider.TicksAbove (horizontal)
#                                   QSlider.TicksBelow (horizontal)
#                                   QSlider.TicksLeft (vertical)
#                                   QSlider.TicksRight (vertical)
#   setTickInterval(interval)   -> Intervalo entre marcas
#   setTracking(bool)           -> Actualiza valor durante drag
#   setInvertedAppearance(bool) -> Invierte dirección
#   setInvertedControls(bool)   -> Invierte teclas de control
#   setOrientation(orientation) -> Cambia orientación
#   setTickPosition(position)   -> Posición de ticks
#   setSliderPosition(val)      -> Posición sin emitir señal
#   hasTracking()              -> Devuelve si hay tracking
#
# Señales:
#   valueChanged(int value)    -> Se emite cuando cambia valor
#   sliderPressed()            -> Se emite al presionar el slider
#   sliderReleased()           -> Se emite al soltar el slider
#   sliderMoved(int value)     -> Se emite al mover (drag)
"""
slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)
slider.setValue(50)
slider.setTickPosition(QSlider.TicksBelow)
slider.setTickInterval(10)
slider.valueChanged.connect(lambda v: print(f"Valor: {v}"))

# -------------------------------------------------------------------
# QDial - Dial giratorio
# -------------------------------------------------------------------
"""
dial = QDial(parent=None)
#
# Es similar a QSlider pero circular.
#
# Métodos principales:
#   setValue(val)               -> Establece valor
#   value()                     -> Devuelve valor
#   setMinimum(val)             -> Valor mínimo
#   minimum()                    -> Devuelve mínimo
#   setMaximum(val)             -> Valor máximo
#   maximum()                    -> Devuelve máximo
#   setRange(min, max)          -> Establece rango
#   setNotchesVisible(bool)     -> Muestra muescas
#   setNotchTarget(target)      -> Tamaño objetivo entre muescas
#   notchSize()                  -> Devuelve tamaño de muesca
#   setWrapping(bool)           -> Permite valores circulares
#   setTracking(bool)           -> Actualiza durante arrastre
#
# Señales:
#   valueChanged(int value)    -> Se emite cuando cambia valor
#   sliderPressed()            -> Se emite al presionar
#   sliderReleased()           -> Se emite al soltar
#   sliderMoved(int value)     -> Se emite al mover
"""
dial = QDial()
dial.setRange(0, 100)
dial.setNotchesVisible(True)
dial.valueChanged.connect(lambda v: print(f"Valor: {v}"))

# -------------------------------------------------------------------
# QLCDNumber - Display numérico estilo LCD
# -------------------------------------------------------------------
"""
lcd = QLCDNumber(parent=None)
# También: QLCDNumber(numDigits, parent=None)
#
# Constructor:
#   - numDigits: número de dígitos a mostrar
#
# Métodos principales:
#   display(value)              -> Muestra valor (int, float, string)
#   setDigitCount(count)        -> Número de dígitos
#   digitCount()                -> Devuelve número de dígitos
#   setMode(mode)               -> Modo de visualización:
#                                   QLCDNumber.Hex
#                                   QLCDNumber.Dec
#                                   QLCDNumber.Oct
#                                   QLCDNumber.Bin
#   mode()                      -> Devuelve modo actual
#   setSegmentStyle(style)      -> Estilo de segmentos:
#                                   QLCDNumber.Outlined
#                                   QLCDNumber.Filled
#                                   QLCDNumber.Flat
#   segmentStyle()              -> Devuelve estilo
#   setSmallDecimalPoint(bool)  -> Punto decimal pequeño
#   smallDecimalPoint()          -> Devuelve si es pequeño
#   checkOverflow(value)        -> Devuelve si el valor desborda
#
# Señales:
#   valueChanged(str value)    -> Se emite al cambiar valor
"""
lcd = QLCDNumber(5)  # 5 dígitos
lcd.display(12345)
lcd.setSegmentStyle(QLCDNumber.Filled)

# -------------------------------------------------------------------
# QProgressBar - Barra de progreso
# -------------------------------------------------------------------
"""
progress = QProgressBar(parent=None)
#
# Métodos principales:
#   setValue(val)               -> Establece valor (0-100 por defecto)
#   value()                     -> Devuelve valor actual
#   setMinimum(val)             -> Valor mínimo
#   minimum()                    -> Devuelve mínimo
#   setMaximum(val)             -> Valor máximo
#   maximum()                    -> Devuelve máximo
#   setRange(min, max)          -> Establece rango
#   reset()                      -> Reinicia a mínimo
#   setOrientation(orientation) -> Orientación (Horizontal/Vertical)
#   setTextVisible(bool)        -> Muestra porcentaje de texto
#   setFormat(format)           -> Formato del texto (%p% por defecto)
#                                   Ej: "%p%" -> "50%"
#                                   Ej: "%p% - %v/%m"
#   format()                    -> Devuelve formato
#   setAlignment(align)         -> Alineación del texto
#   setInvertedAppearance(bool) -> Invierte dirección de progreso
#   setMinimumWidth(width)     -> Ancho mínimo
#   setMaximumWidth(width)     -> Ancho máximo
#   setMinimumHeight(height)   -> Alto mínimo
#
# Señales:
#   valueChanged(int value)    -> Se emite al cambiar valor
"""
progress = QProgressBar()
progress.setRange(0, 100)
progress.setValue(50)
progress.setFormat("%p% completado")
progress.valueChanged.connect(lambda v: print(f"Progreso: {v}%"))

# ============================================================================
# WIDGETS DE FECHA Y HORA
# ============================================================================

# -------------------------------------------------------------------
# QDateEdit - Editor de fecha
# -------------------------------------------------------------------
"""
dateedit = QDateEdit(parent=None)
# También: QDateEdit(date, parent=None)
#
# Métodos principales:
#   setDate(date)               -> Establece fecha
#   date()                       -> Devuelve fecha (QDate)
#   setMinimumDate(date)        -> Fecha mínima
#   minimumDate()                -> Devuelve fecha mínima
#   setMaximumDate(date)        -> Fecha máxima
#   maximumDate()                -> Devuelve fecha máxima
#   setDateRange(min, max)      -> Rango de fechas
#   setCalendarPopup(bool)      -> Muestra calendario popup
#   calendarPopup()              -> Devuelve si hay popup
#   setDisplayFormat(format)    -> Formato de visualización
#                                   Ej: "yyyy-MM-dd" -> "2024-01-15"
#                                   Ej: "dd/MM/yyyy" -> "15/01/2024"
#   displayFormat()              -> Devuelve formato
#   setSelectedSection(section) -> Sección seleccionada
#
# Señales:
#   dateChanged(QDate date)    -> Se emite al cambiar fecha
#   dateTimeChanged(QDateTime) -> Se emite al cambiar fecha/hora
"""
from PyQt5.QtCore import QDate
dateedit = QDateEdit()
dateedit.setDate(QDate.currentDate())
dateedit.setCalendarPopup(True)
dateedit.setDisplayFormat("dd/MM/yyyy")

# -------------------------------------------------------------------
# QTimeEdit - Editor de hora
# -------------------------------------------------------------------
"""
timeedit = QTimeEdit(parent=None)
# También: QTimeEdit(time, parent=None)
#
# Métodos principales:
#   setTime(time)               -> Establece hora
#   time()                       -> Devuelve hora (QTime)
#   setMinimumTime(time)        -> Hora mínima
#   minimumTime()                -> Devuelve hora mínima
#   setMaximumTime(time)        -> Hora máxima
#   maximumTime()                -> Devuelve hora máxima
#   setTimeRange(min, max)      -> Rango de horas
#   setDisplayFormat(format)    -> Formato
#                                   Ej: "HH:mm" -> "14:30"
#                                   Ej: "hh:mm:ss AP" -> "02:30:45 PM"
#   displayFormat()              -> Devuelve formato
#
# Señales:
#   timeChanged(QTime time)    -> Se emite al cambiar hora
"""
from PyQt5.QtCore import QTime
timeedit = QTimeEdit()
timeedit.setTime(QTime.currentTime())
timeedit.setDisplayFormat("HH:mm:ss")

# -------------------------------------------------------------------
# QDateTimeEdit - Editor de fecha y hora
# -------------------------------------------------------------------
"""
datetimeedit = QDateTimeEdit(parent=None)
# También: QDateTimeEdit(datetime, parent=None)
#
# Combina funcionalidad de QDateEdit y QTimeEdit
#
# Métodos principales:
#   setDateTime(datetime)       -> Establece fecha y hora
#   dateTime()                   -> Devuelve QDateTime
#   setDate(date)               -> Establece solo fecha
#   setTime(time)               -> Establece solo hora
#   date()                       -> Devuelve QDate
#   time()                       -> Devuelve QTime
#   setMinimumDateTime(datetime) -> Fecha/hora mínima
#   setMaximumDateTime(datetime) -> Fecha/hora máxima
#   setDateTimeRange(min, max)   -> Rango completo
#   setCalendarPopup(bool)      -> Popup de calendario
#   setDisplayFormat(format)    -> Formato de visualización
#                                   Ej: "dd/MM/yyyy HH:mm"
#
# Señales:
#   dateTimeChanged(QDateTime)  -> Se emite al cambiar fecha/hora
#   dateChanged(QDate)          -> Se emite al cambiar fecha
#   timeChanged(QTime)          -> Se emite al cambiar hora
"""
from PyQt5.QtCore import QDateTime
datetimeedit = QDateTimeEdit()
datetimeedit.setDateTime(QDateTime.currentDateTime())
datetimeedit.setDisplayFormat("dd/MM/yyyy HH:mm")

# -------------------------------------------------------------------
# QFontComboBox - Selector de fuente
# -------------------------------------------------------------------
"""
fontcombo = QFontComboBox(parent=None)
#
# Lista desplegable con todas las fuentes del sistema
#
# Métodos principales:
#   setFontFilters(filters)    -> Filtros de fuentes:
#                                   QFontComboBox.AllFonts
#                                   QFontComboBox.ScalableFonts
#                                   QFontComboBox.NonScalableFonts
#                                   QFontComboBox.MonospacedFonts
#                                   QFontComboBox.ProportionalFonts
#   fontFilters()               -> Devuelve filtros actuales
#   currentFont()              -> Fuente actual (QFont)
#   setCurrentFont(font)       -> Establece fuente actual
#   currentIndex()             -> Índice actual
#   setCurrentIndex(index)     -> Establece índice
#
# Señales:
#   currentFontChanged(QFont)  -> Se emite al cambiar fuente
"""
fontcombo = QFontComboBox()
fontcombo.setFontFilters(QFontComboBox.MonospacedFonts)
fontcombo.currentFontChanged.connect(lambda f: print(f"Fuente: {f.family()}"))

# ============================================================================
# WIDGETS DE LISTAS Y COMBOBOX
# ============================================================================

# -------------------------------------------------------------------
# QComboBox - Lista desplegable
# -------------------------------------------------------------------
"""
combobox = QComboBox(parent=None)
#
# Métodos principales:
#   addItem(text, userData=None) -> Añade un elemento
#   addItems(list_of_text)      -> Añade varios elementos
#   insertItem(index, text, userData=None) -> Inserta en posición
#   insertItems(index, list)    -> Inserta varios
#   removeItem(index)          -> Elimina elemento
#   clear()                      -> Elimina todos los elementos
#   setItemText(index, text)   -> Cambia texto de elemento
#   itemText(index)             -> Devuelve texto de elemento
#   setItemData(index, data)    -> Asigna dato asociado
#   itemData(index)            -> Devuelve dato asociado
#   setCurrentIndex(index)      -> Establece índice actual
#   currentIndex()              -> Devuelve índice actual
#   currentText()              -> Devuelve texto actual
#   setCurrentText(text)        -> Establece texto actual (busca coincidencia)
#   count()                     -> Número de elementos
#   setMaxCount(max)           -> Máximo de elementos
#   maxCount()                  -> Devuelve máximo
#   setEditable(bool)           -> Permite edición
#   setInsertPolicy(policy)    -> Política de inserción:
#                                   QComboBox.NoInsert
#                                   QComboBox.InsertAtTop
#                                   QComboBox.InsertAtCurrent
#                                   QComboBox.InsertAtBottom
#                                   QComboBox.InsertAfterCurrent
#                                   QComboBox.InsertBeforeCurrent
#                                   QComboBox.InsertAlphabetically
#   setDuplicatesEnabled(bool)  -> Permite duplicados
#   setSizeAdjustPolicy(policy) -> Ajuste de tamaño:
#                                   QComboBox.AdjustToContents
#                                   QComboBox.AdjustToMinimumContentsLength
#                                   QComboBox.AdjustToMinimumContentsLengthWithIcon
#   setPlaceholderText(text)    -> Texto cuando está vacío
#   model()                     -> Modelo de datos
#   setModel(model)            -> Establece modelo (para QAbstractItemModel)
#   findText(text)             -> Busca texto, devuelve índice o -1
#   findData(data)             -> Busca dato, devuelve índice o -1
#
# Señales:
#   currentIndexChanged(int index) -> Índice cambió
#   currentTextChanged(str text)   -> Texto cambió
#   activated(int index)        -> Usuario selecciona (antes de aplicar)
#   highlighted(int index)      -> Elemento resaltado
#   editTextChanged(str text)   -> Texto en modo editable cambió
"""
combobox = QComboBox()
combobox.addItem("Opción 1")
combobox.addItem("Opción 2")
combobox.addItems(["Opción 3", "Opción 4"])
combobox.setCurrentIndex(0)
combobox.currentIndexChanged.connect(lambda i: print(f"Índice: {i}"))

# -------------------------------------------------------------------
# QListWidget - Lista de elementos (con gestión interna)
# -------------------------------------------------------------------
"""
listwidget = QListWidget(parent=None)
#
# Lista con modelo interno (fácil de usar)
#
# Métodos principales:
#   addItem(label)              -> Añade string
#   addItems(list_of_labels)   -> Añade varios strings
#   insertItem(row, item)       -> Inserta en fila
#   insertItems(row, list)     -> Inserta varios
#   takeItem(row)              -> Elimina y devuelve item
#   clear()                      -> Elimina todos
#   currentItem()              -> Item actual
#   currentRow()               -> Fila actual
#   setCurrentItem(item)        -> Establece item actual
#   setCurrentRow(row)         -> Establece fila actual
#   row(item)                   -> Devuelve fila de item
#   count()                     -> Número de items
#   item(row)                   -> Devuelve item de fila
#   selectedItems()            -> Lista de items seleccionados
#   currentItemChanged(item, previous) -> Señal de cambio de item
#   setSelectionMode(mode)     -> Modo de selección:
#                                   QAbstractItemView.SingleSelection
#                                   QAbstractItemView.ContiguousSelection
#                                   QAbstractItemView.MultiSelection
#                                   QAbstractItemView.ExtendedSelection
#                                   QAbstractItemView.NoSelection
#   setDragDropMode(mode)      -> Modo drag & drop:
#                                   QAbstractItemView.NoDragDrop
#                                   QAbstractItemView.DragOnly
#                                   QAbstractItemView.DropOnly
#                                   QAbstractItemView.DragDrop
#   sortItems(order)           -> Ordena (Qt.AscendingOrder, Qt.DescendingOrder)
#   isSortingEnabled()         -> Devuelve si hay ordenación
#   setSortingEnabled(bool)    -> Habilita/deshabilita ordenación
#
# Señales:
#   currentItemChanged(QListWidgetItem*, QListWidgetItem*) -> Item actual cambió
#   currentRowChanged(int row) -> Fila actual cambió
#   itemClicked(QListWidgetItem*) -> Click en item
#   itemDoubleClicked(QListWidgetItem*) -> Doble click
#   itemSelectionChanged()      -> Selección cambió
#   itemChanged(QListWidgetItem*) -> Item cambió
#   itemEntered(QListWidgetItem*) -> Ratón entró en item
"""
listwidget = QListWidget()
listwidget.addItem("Elemento 1")
listwidget.addItem("Elemento 2")
listwidget.setSelectionMode(QListWidget.MultiSelection)
listwidget.itemClicked.connect(lambda item: print(f"Clic: {item.text()}"))

# -------------------------------------------------------------------
# QTableView - Vista de tabla (requiere modelo)
# -------------------------------------------------------------------
"""
tableview = QTableView(parent=None)
#
# Vista de tabla que necesita un modelo de datos (Model-View)
#
# Métodos principales:
#   setModel(model)            -> Establece modelo
#   model()                     -> Devuelve modelo
#   setSelectionModel(selModel) -> Modelo de selección
#   selectionModel()            -> Devuelve modelo de selección
#   setSelectionBehavior(behavior) -> Comportamiento de selección:
#                                       SelectRows
#                                       SelectColumns
#                                       SelectItems
#   setSelectionMode(mode)      -> Modo de selección
#   setEditTriggers(triggers)  -> Disparadores de edición:
#                                   QAbstractItemView.NoEditTriggers
#                                   QAbstractItemView.CurrentChanged
#                                   QAbstractItemView.DoubleClicked
#                                   QAbstractItemView.SelectedClicked
#                                   QAbstractItemView.EditKeyPressed
#                                   QAbstractItemView.AnyKeyPressed
#                                   QAbstractItemView.AllEditTriggers
#   setGridStyle(style)        -> Estilo de líneas de cuadrícula
#   setCornerButtonEnabled(bool) -> Botón de esquina
#   setColumnWidth(column, width) -> Ancho de columna
#   setRowHeight(row, height)  -> Alto de fila
#   setColumnHidden(column, hide) -> Oculta/mostra columna
#   setRowHidden(row, hide)    -> Oculta/mostra fila
#   resizeColumnToContents(column) -> Ajusta columna
#   resizeRowToContents(row)   -> Ajusta fila
#   resizeColumnsToContents()  -> Ajusta todas las columnas
#   sortByColumn(column, order) -> Ordena por columna
#   setSortingEnabled(bool)    -> Habilita ordenación
#   selectedIndexes()          -> Lista de índices seleccionados
#   currentIndex()            -> Índice actual
#   clearSelection()          -> Limpia selección
#   selectAll()                -> Selecciona todo
#
# Señales:
#   clicked(const QModelIndex&) -> Click en celda
#   doubleClicked(const QModelIndex&) -> Doble click
#   activated(const QModelIndex&) -> Activado
#   entered(const QModelIndex&) -> Entró con ratón
#   viewportEntered()          -> Viewport entrou
"""
# Ejemplo con QStandardItemModel
model = QStandardItemModel(3, 3)  # 3 filas, 3 columnas
tableview = QTableView()
tableview.setModel(model)
tableview.setEditTriggers(QTableView.NoEditTriggers)

# Llenar modelo
for row in range(3):
    for col in range(3):
        item = QStandardItem(f"Fila {row}, Col {col}")
        model.setItem(row, col, item)

# -------------------------------------------------------------------
# QListView - Vista de lista (requiere modelo)
# -------------------------------------------------------------------
"""
listview = QListView(parent=None)
#
# Vista de lista que necesita un modelo (Model-View)
#
# Métodos principales:
#   setModel(model)            -> Establece modelo
#   model()                     -> Devuelve modelo
#   setItemDelegate(delegate)  -> Establece delegado
#   setSelectionModel(selModel) -> Modelo de selección
#   selectionModel()            -> Devuelve modelo de selección
#   setSelectionMode(mode)      -> Modo de selección
#   setViewMode(mode)          -> Modo de vista:
#                                   QListView.ListMode
#                                   QListView.IconMode
#   viewMode()                  -> Devuelve modo
#   setGridSize(size)          -> Tamaño de celdas en IconMode
#   gridSize()                  -> Devuelve tamaño de celdas
#   setSpacing(spacing)        -> Espaciado entre items
#   spacing()                  -> Devuelve espaciado
#   setFlow(flow)              -> Flujo:
#                                   QListView.LeftToRight
#                                   QListView.TopToBottom
#   setWrapping(bool)          -> Permite wrapping
#   setResizeMode(mode)        -> Modo de redimensión:
#                                   QListView.Fixed
#                                   QListView.Adjust
#   setMovement(mode)          -> Movimiento:
#                                   QListView.Static
#                                   QListView.Free
#                                   QListView.Snap
#   selectedIndexes()          -> Lista de índices seleccionados
#   currentIndex()            -> Índice actual
"""
listview = QListView()
listview.setViewMode(QListView.ListMode)
listview.setSelectionMode(QListView.ExtendedSelection)

# ============================================================================
# WIDGETS DE PESTAÑAS
# ============================================================================

# -------------------------------------------------------------------
# QTabWidget - Widget con pestañas
# -------------------------------------------------------------------
"""
tabwidget = QTabWidget(parent=None)
#
# Métodos principales:
#   addTab(page, label)        -> Añade pestaña con widget y etiqueta
#   insertTab(index, page, label) -> Inserta pestaña
#   removeTab(index)          -> Elimina pestaña
#   clear()                      -> Elimina todas las pestañas
#   setTabText(index, text)   -> Establece texto de pestaña
#   tabText(index)             -> Devuelve texto de pestaña
#   setTabIcon(index, icon)    -> Establece icono
#   tabIcon(index)             -> Devuelve icono
#   setTabToolTip(index, tip)  -> Tooltip de pestaña
#   setTabEnabled(index, bool) -> Habilita/deshabilita pestaña
#   isTabEnabled(index)        -> Devuelve si está habilitada
#   setTabVisible(index, bool) -> Muestra/oculta pestaña
#   isTabVisible(index)        -> Devuelve si está visible
#   setCurrentIndex(index)     -> Establece pestaña activa
#   currentIndex()              -> Devuelve índice actual
#   currentWidget()            -> Devuelve widget actual
#   setCurrentWidget(widget)   -> Establece widget actual
#   widget(index)              -> Devuelve widget de índice
#   indexOf(widget)            -> Devuelve índice de widget
#   count()                     -> Número de pestañas
#   setTabPosition(position)   -> Posición de pestañas:
#                                   QTabWidget.North (arriba)
#                                   QTabWidget.South (abajo)
#                                   QTabWidget.West (izquierda)
#                                   QTabWidget.East (derecha)
#   tabPosition()              -> Devuelve posición
#   setTabShape(shape)         -> Forma de pestañas:
#                                   QTabWidget.Rounded (redondeadas)
#                                   QTabWidget.Triangular
#   setDocumentMode(bool)      -> Modo documento (sin marco)
#   setMovable(bool)           -> Pestañas movibles
#   setUsesScrollButtons(bool) -> Botones de scroll si hay muchas pestañas
#   setIconSize(size)          -> Tamaño de icono de pestañas
#
# Señales:
#   currentChanged(int index)  -> Índice cambió
#   tabCloseRequested(int index) -> Pestaña pide cerrar
#   tabMoved(int from, int to) -> Pestaña movida
"""
tabwidget = QTabWidget()
tabwidget.setTabPosition(QTabWidget.North)

# Crear pestañas
for i, color in enumerate(["Rojo", "Verde", "Azul"]):
    page = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QLabel(f"Contenido de {color}"))
    page.setLayout(layout)
    tabwidget.addTab(page, color)

tabwidget.currentChanged.connect(lambda i: print(f"Pestaña: {i}"))

# ============================================================================
# MENÚS Y BARRAS DE HERRAMIENTAS
# ============================================================================

# -------------------------------------------------------------------
# QMenuBar - Barra de menú (normalmente integrada en QMainWindow)
# -------------------------------------------------------------------
"""
menubar = window.menuBar()  # Desde QMainWindow
# o
menubar = QMenuBar(parent)
#
# Métodos principales:
#   addMenu(title_or_menu)     -> Añade menú (devuelve QMenu)
#   insertMenu(before, menu)   -> Inserta menú antes de otro
#   removeMenu(menu)          -> Elimina menú
#   clear()                      -> Elimina todos los menús
#   setCornerWidget(widget, corner) -> Widget en esquina:
#                                       Qt.TopLeftCorner
#                                       Qt.TopRightCorner
#                                       Qt.BottomLeftCorner
#                                       Qt.BottomRightCorner
#   isVisible()                -> Devuelve si es visible
#   setVisible(bool)           -> Muestra/oculta
#
# Señales:
#   hovered(menu)              -> Ratón sobre menú
#   triggered(action)          -> Acción activada
"""
menubar = window.menuBar()
file_menu = menubar.addMenu("&Fichero")  # & crea atajo de teclado (Alt+F)

# -------------------------------------------------------------------
# QMenu - Menú desplegable
# -------------------------------------------------------------------
"""
menu = QMenu(title="", parent=None)
# o desde menubar:
menu = menubar.addMenu("&Archivo")
#
# Métodos principales:
#   setTitle(title)            -> Establece título
#   title()                     -> Devuelve título
#   addAction(action)          -> Añade acción
#   addActions(list_of_actions) -> Añade varias acciones
#   addSeparator()             -> Añade separador
#   addMenu(title)            -> Crea y añade submenú
#   addMenu(menu)             -> Añade submenú existente
#   insertMenu(before, menu)   -> Inserta menú
#   insertSeparator(before)   -> Inserta separador
#   removeAction(action)      -> Elimina acción
#   clear()                      -> Elimina todas las acciones
#   setIcon(icon)             -> Establece icono
#   exec()                      -> Muestra menú (bloqueante)
#   exec(pos)                  -> Muestra menú en posición
#   popup(pos)                 -> Muestra menú (alternativa)
#   isEmpty()                  -> Devuelve si está vacío
#   menuAction()              -> Devuelve QAction del menú
#
# Señales:
#   triggered(action)         -> Acción del menú activada
#   hovered(action)           -> Acción resaltada
#   aboutToShow()             -> Menú a punto de mostrarse
#   aboutToHide()             -> Menú a punto de ocultarse
"""
menu = QMenu()
menu.setTitle("Archivo")
menu.addAction(action)
menu.addSeparator()

# Submenú
submenu = menu.addMenu("Submenú")

# -------------------------------------------------------------------
# QAction - Acción (puede ir en menú, toolbar, botón)
# -------------------------------------------------------------------
"""
action = QAction(icon_or_text, parent=None)
# Formas:
#   QAction(text, parent)
#   QAction(icon, text, parent)
#
# Constructor con parámetros:
#   - icon: QIcon (opcional)
#   - text: texto de la acción
#   - parent: widget padre
#
# Métodos principales:
#   setText(text)              -> Establece texto
#   text()                      -> Devuelve texto
#   setIcon(icon)              -> Establece icono
#   icon()                      -> Devuelve icono
#   setShortcut(keysequence)   -> Establece atajo de teclado
#   shortcut()                  -> Devuelve atajo
#   setToolTip(tip)           -> Tooltip
#   toolTip()                   -> Devuelve tooltip
#   setStatusTip(tip)          -> Tooltip de barra de estado
#   statusTip()                 -> Devuelve tooltip de estado
#   setData(data)             -> Establece dato arbitrario
#   data()                      -> Devuelve dato
#   setCheckable(bool)         -> Marcarlo/desmarcarlo
#   setChecked(bool)           -> Establece estado checked
#   isChecked()                -> Devuelve si está checked
#   setEnabled(bool)           -> Habilita/deshabilita
#   isEnabled()                -> Devuelve si está habilitado
#   setVisible(bool)           -> Muestra/oculta
#   setSeparator(bool)         -> Es separador
#   trigger()                  -> Activa la acción (simula click)
#   setIconVisibleInMenu(bool) -> Muestra icono en menú
#   setShortcutContext(context) -> Contexto de atajo:
#                                   Qt.WidgetWithChildrenShortcut
#                                   Qt.WindowShortcut
#                                   Qt.ApplicationShortcut
#                                   Qt.AA_DisableShortcutIntegration
#
# Señales:
#   triggered(bool checked=False) -> Acción activada
#   toggled(bool checked)       -> Estado changed (si checkable)
"""
action = QAction(QIcon("icon.png"), "&Abrir", window)
action.setStatusTip("Abrir archivo")
action.setShortcut(QKeySequence("Ctrl+O"))
action.setCheckable(True)
action.triggered.connect(lambda checked: print(f"Triggered: {checked}"))

# -------------------------------------------------------------------
# QToolBar - Barra de herramientas
# -------------------------------------------------------------------
"""
toolbar = QToolBar(title="", parent=None)
# o desde QMainWindow:
toolbar = QToolBar("Toolbar")
window.addToolBar(toolbar)
#
# Métodos principales:
#   setWindowTitle(title)      -> Título de la barra
#   addAction(action)          -> Añade acción
#   addActions(list)           -> Añade varias acciones
#   addSeparator()             -> Añade separador
#   addWidget(widget)         -> Añade widget
#   addBreak()                 -> Añade ruptura (nueva línea/columna)
#   insertAction(before, action) -> Inserta acción
#   insertSeparator(before)    -> Inserta separador
#   insertWidget(before, widget) -> Inserta widget
#   removeAction(action)      -> Elimina acción
#   clear()                      -> Elimina todo
#   setIconSize(size)         -> Tamaño de iconos
#   iconSize()                  -> Devuelve tamaño
#   setMovable(bool)          -> Bar movible
#   isMovable()                -> Devuelve si es movible
#   setFloatable(bool)        -> Puede flotar
#   isFloatable()              -> Devuelve si flota
#   setAllowedAreas(areas)    -> Áreas permitidas:
#                                   Qt.LeftToolBarArea
#                                   Qt.RightToolBarArea
#                                   Qt.TopToolBarArea
#                                   Qt.BottomToolBarArea
#                                   Qt.AllToolBarAreas
#                                   Qt.NoToolBarArea
#   allowedAreas()             -> Devuelve áreas
#   setToolButtonStyle(style)  -> Estilo de botones:
#                                   Qt.ToolButtonIconOnly
#                                   Qt.ToolButtonTextOnly
#                                   Qt.ToolButtonTextBesideIcon
#                                   Qt.ToolButtonTextUnderIcon
#                                   Qt.ToolButtonFollowStyle
#   toolButtonStyle()          -> Devuelve estilo
#   toggleViewAction()        -> Acción para mostrar/ocultar
#
# Señales:
#   actionTriggered(action)    -> Acción activada
#   movableChanged(bool)       -> Cambió si es movible
#   floatableChanged(bool)    -> Cambió si es flotable
#   iconSizeChanged(QSize)     -> Tamaño de icono cambió
#   toolButtonStyleChanged(Qt.ToolButtonStyle) -> Estilo cambió
"""
toolbar = QToolBar("Mi Toolbar")
toolbar.setIconSize(QSize(32, 32))
toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
toolbar.addAction(action)

# -------------------------------------------------------------------
# QStatusBar - Barra de estado
# -------------------------------------------------------------------
"""
statusbar = window.statusBar()  # Desde QMainWindow
# o
statusbar = QStatusBar(parent=None)
window.setStatusBar(statusbar)
#
# Métodos principales:
#   showMessage(text, timeout=0) -> Muestra mensaje temporal
#                                   timeout en ms, 0 = permanente
#   clearMessage()             -> Limpia mensaje actual
#   addWidget(widget, stretch=0) -> Añade widget permanente
#   addPermanentWidget(widget, stretch=0) -> Añade widget no temporal
#   insertWidget(index, widget, stretch=0) -> Inserta widget
#   removeWidget(widget)       -> Elimina widget
#   setSizeGripEnabled(bool)   -> Muestra grip de redimensión
#   isSizeGripEnabled()        -> Devuelve si hay grip
#   setStyleSheet(stylesheet)  -> Estilo CSS
#
# Señales:
#   messageChanged(const QString&) -> Mensaje cambió
"""
statusbar = window.statusBar()
statusbar.showMessage("Listo", 3000)  # 3 segundos
statusbar.addWidget(QLabel("Permanente"))

# ============================================================================
# DIÁLOGOS
# ============================================================================

# -------------------------------------------------------------------
# QMessageBox - Diálogo de mensaje
# -------------------------------------------------------------------
"""
msgbox = QMessageBox(parent=None)
# Tipos:
#   QMessageBox(parent).setXxx() para configurar
#
# Métodos principales:
#   setWindowTitle(title)      -> Título de la ventana
#   setText(text)              -> Texto principal
#   setInformativeText(text)   -> Texto informativo adicional
#   setDetailedText(text)      -> Texto detallado (expandible)
#   setIcon(icon)              -> Icono:
#                                   QMessageBox.NoIcon
#                                   QMessageBox.Information
#                                   QMessageBox.Warning
#                                   QMessageBox.Critical
#                                   QMessageBox.Question
#   setStandardButtons(buttons) -> Botones estándar:
#                                   QMessageBox.Ok
#                                   QMessageBox.Cancel
#                                   QMessageBox.Yes
#                                   QMessageBox.No
#                                   QMessageBox.Abort
#                                   QMessageBox.Retry
#                                   QMessageBox.Ignore
#                                   QMessageBox.Close
#                                   QMessageBox.YesToAll
#                                   QMessageBox.NoToAll
#                                   QMessageBox.NoButton
#                                   Combinar con | : QMessageBox.Yes | QMessageBox.No
#   setDefaultButton(button)   -> Botón por defecto
#   setEscapeButton(button)    -> Botón de escape (Escape)
#   setButtonText(button, text) -> Texto de botón
#   button(button)             -> Devuelve botón
#   exec()                      -> Muestra diálogo modal, devuelve botón presionado
#
# Métodos estáticos (más fáciles de usar):
#   QMessageBox.information(parent, title, text, buttons, defaultButton)
#   QMessageBox.question(parent, title, text, buttons, defaultButton)
#   QMessageBox.warning(parent, title, text, buttons, defaultButton)
#   QMessageBox.critical(parent, title, text, buttons, defaultButton)
#   QMessageBox.about(parent, title, text)  -> Acerca de
#   QMessageBox.aboutQt(parent, title="")   -> Acerca de Qt
#
# Constantes de botón:
#   QMessageBox.Ok
#   QMessageBox.Cancel
#   QMessageBox.Yes
#   QMessageBox.No
#   QMessageBox.YesToAll
#   QMessageBox.NoToAll
#   QMessageBox.Abort
#   QMessageBox.Retry
#   QMessageBox.Ignore
#   QMessageBox.NoButton
"""
# Forma estática
button = QMessageBox.question(
    window,
    "Confirmar",
    "¿Desea guardar los cambios?",
    QMessageBox.Yes | QMessageBox.No,
    QMessageBox.No  # botón por defecto
)
if button == QMessageBox.Yes:
    print("Guardar")

# Forma con diálogo configurado
dialog = QMessageBox(window)
dialog.setWindowTitle("Error")
dialog.setText("Ha ocurrido un error")
dialog.setInformativeText("¿Qué desea hacer?")
dialog.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
dialog.setDefaultButton(QMessageBox.Retry)
if dialog.exec() == QMessageBox.Retry:
    print("Reintentar")

# -------------------------------------------------------------------
# QFileDialog - Diálogo de archivo
# -------------------------------------------------------------------
"""
filedialog = QFileDialog(parent=None)
#
# Métodos estáticos:
#   getOpenFileName(parent, title, dir, filter, options)
#       -> Devuelve tupla (ruta, filtro) o ("", "")
#   getOpenFileNames(parent, title, dir, filter, options)
#       -> Devuelve tupla (lista_rutas, filtro)
#   getSaveFileName(parent, title, dir, filter, options)
#       -> Devuelve tupla (ruta, filtro) o ("", "")
#   getExistingDirectory(parent, title, dir, options)
#       -> Devuelve ruta o ""
#
# Parámetros:
#   - parent: widget padre
#   - title: título del diálogo
#   - dir: directorio inicial
#   - filter: filtro de archivos (ej: "Archivos texto (*.txt);;Todos (*.*)")
#   - options: opciones de QFileDialog
#
# Opciones:
#   QFileDialog.ShowDirsOnly
#   QFileDialog.DontResolveSymlinks
#   QFileDialog.DontConfirmOverwrite
#   QFileDialog.DontUseNativeDialog
#   QFileDialog.SingleDir
#   QFileDialog.SingleFile
#   QFileDialog.ExistingFiles
#
# Métodos de instancia:
#   setDirectory(dir)          -> Directorio
#   setNameFilter(filter)      -> Filtro
#   setFileMode(mode)          -> Modo:
#                                   QFileDialog.AnyFile
#                                   QFileDialog.ExistingFile
#                                   QFileDialog.Directory
#                                   QFileDialog.ExistingFiles
#                                   QFileDialog.DirectoryOnly
#   fileMode()                  -> Devuelve modo
#   setAcceptMode(mode)        -> Modo de aceptación:
#                                   QFileDialog.AcceptOpen
#                                   QFileDialog.AcceptSave
#   acceptMode()              -> Devuelve modo
#   selectedFiles()            -> Lista de archivos seleccionados
#   selectedNameFilter()       -> Filtro seleccionado
#   exec()                      -> Muestra diálogo
"""
# Abrir archivo (devuelve tupla)
filename, _ = QFileDialog.getOpenFileName(
    window,
    "Abrir archivo",
    "/home",
    "Archivos texto (*.txt);;Todos (*.*)"
)
if filename:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

# Guardar archivo
filename, _ = QFileDialog.getSaveFileName(
    window,
    "Guardar archivo",
    "",
    "Archivos texto (*.txt);;Todos (*.*)"
)
if filename:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("contenido")

# Seleccionar directorio
directory = QFileDialog.getExistingDirectory(window, "Seleccionar directorio")

# -------------------------------------------------------------------
# QDialog - Diálogo genérico
# -------------------------------------------------------------------
"""
dialog = QDialog(parent=None)
#
# Es la clase base para diálogos. Todos los diálogos heredan de QDialog.
#
# Métodos principales:
#   setWindowTitle(title)      -> Título
#   setModal(bool)             -> Si es modal (bloquea padre)
#   isModal()                  -> Devuelve si es modal
#   setResult(result)          -> Establece resultado (aceptado/rechazado)
#   result()                   -> Devuelve resultado
#   accept()                    -> Acepta y cierra (result = Accepted)
#   reject()                    -> Rechaza y cierra (result = Rejected)
#   done(result)               -> Cierra con código de resultado
#   exec()                      -> Muestra diálogo modal (bloqueante)
#   open()                      -> Muestra diálogo no modal
#   show()                      -> Muestra (no modal)
#   setSizeGripEnabled(bool)   -> Grip de redimensión
#   setFixedSize(w, h)         -> Tamaño fijo
#   setMinimumSize(w, h)       -> Tamaño mínimo
#   setMaximumSize(w, h)       -> Tamaño máximo
#
# Señales:
#   accepted()                  -> Diálogo aceptado
#   rejected()                  -> Diálogo rechazado
#   finished(result)           -> Diálogo cerrado con resultado
#   rejected()                  -> Se emite en reject()
#
# Constantes de resultado:
#   QDialog.Accepted (= 1)
#   QDialog.Rejected (= 0)
"""
dialog = QDialog(window)
dialog.setModal(True)
dialog.setWindowTitle("Mi Diálogo")

# Configurar contenido
layout = QVBoxLayout()
layout.addWidget(QLabel("Contenido del diálogo"))
dialog.setLayout(layout)

if dialog.exec() == QDialog.Accepted:
    print("Aceptado")
else:
    print("Rechazado")

# ============================================================================
# LAYOUTS
# ============================================================================

# -------------------------------------------------------------------
# QVBoxLayout - Layout vertical (elementos apilados verticalmente)
# -------------------------------------------------------------------
"""
layout = QVBoxLayout(parent=None)
#
# Métodos principales:
#   addWidget(widget, stretch=0, alignment=0)
#       -> Añade widget con factor de estiramiento opcional
#   addLayout(layout, stretch=0)
#       -> Añade sub-layout
#   addStrut(size)             -> Espaciador rígido
#   addSpacing(size)           -> Espacio entre widgets
#   addStretch(stretch=0)      -> Espaciador elástico
#   insertWidget(index, widget, stretch=0, alignment=0)
#       -> Inserta widget en posición
#   insertLayout(index, layout, stretch=0)
#   insertSpacing(index, size)
#   insertStretch(index, stretch=0)
#   removeWidget(widget)       -> Elimina widget
#   removeItem(item)           -> Elimina item (incluye espaciadores)
#   count()                     -> Número de items
#   itemAt(index)              -> Item en índice
#   takeAt(index)              -> Elimina y devuelve item
#   setSpacing(spacing)        -> Espaciado entre widgets
#   spacing()                  -> Devuelve espaciado
#   setContentsMargins(left, top, right, bottom)
#       -> Márgenes del layout
#   setContentsMargins(QMargins)
#   contentsMargins()          -> Devuelve márgenes
#   setStretchFactor(widget_or_layout, stretch)
#       -> Factor de estiramiento
#   setAlignment(alignment)     -> Alineación del layout
#   setDirection(direction)    -> Dirección:
#                                   QBoxLayout.TopToBottom (por defecto)
#                                   QBoxLayout.BottomToTop
#   direction()                -> Devuelve dirección
"""
layout_v = QVBoxLayout()
layout_v.addWidget(QLabel("Arriba"))
layout_v.addWidget(QLabel("Centro"))
layout_v.addWidget(QLabel("Abajo"))
layout_v.addStretch()  # Empuja widgets hacia arriba

# -------------------------------------------------------------------
# QHBoxLayout - Layout horizontal (elementos en fila)
# -------------------------------------------------------------------
"""
layout = QHBoxLayout(parent=None)
#
# Mismos métodos que QVBoxLayout, pero apila horizontalmente.
#
# Dirección:
#   QBoxLayout.LeftToRight (por defecto)
#   QBoxLayout.RightToLeft
"""
layout_h = QHBoxLayout()
layout_h.addWidget(QLabel("Izquierda"))
layout_h.addWidget(QLabel("Centro"))
layout_h.addWidget(QLabel("Derecha"))
layout_h.addStretch()  # Empuja widgets hacia la izquierda

# -------------------------------------------------------------------
# QGridLayout - Layout en cuadrícula (filas y columnas)
# -------------------------------------------------------------------
"""
layout = QGridLayout(parent=None)
#
# Métodos principales:
#   addWidget(widget, row, column, rowSpan=1, columnSpan=1, alignment=0)
#       -> Añade widget en celda (fila, columna)
#   addWidget(widget, fromRow, fromCol, rowSpan, colSpan, alignment=0)
#       -> Añade widget ocupando varias celdas
#   addLayout(layout, row, column, rowSpan=1, columnSpan=1, alignment=0)
#       -> Añade sub-layout
#   addItem(item, row, column, rowSpan=1, columnSpan=1, alignment=0)
#   setRowStretch(row, stretch)
#   setColumnStretch(column, stretch)
#       -> Factor de estiramiento de fila/columna
#   setRowMinimumHeight(row, minSize)
#   setColumnMinimumWidth(column, minSize)
#       -> Altura/ancho mínimo de fila/columna
#   setSpacing(spacing)        -> Espaciado entre celdas
#   setHorizontalSpacing(spacing)
#   setVerticalSpacing(spacing)
#   rowCount()                  -> Número de filas
#   columnCount()              -> Número de columnas
#   itemAtPosition(row, col)   -> Item en posición
#   getItemPosition(index)     -> Posición de item (devuelve tupla row, col, rowSpan, colSpan)
#   removeWidget(widget)       -> Elimina widget
#
# Notas:
#   - Filas y columnas empiezan en 0
#   - Widgets pueden ocupar múltiples celdas con rowSpan/colSpan
#   - Alignment: Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignTop, Qt.AlignBottom, Qt.AlignVCenter, Qt.AlignCenter
"""
layout_grid = QGridLayout()

# Añadir widgets
layout_grid.addWidget(QLabel("0,0"), 0, 0)
layout_grid.addWidget(QLabel("0,1"), 0, 1)
layout_grid.addWidget(QLabel("1,0"), 1, 0)
layout_grid.addWidget(QLabel("1,1"), 1, 1)

# Ocupar múltiples celdas
layout_grid.addWidget(QLabel("Ocupo 2 columnas"), 2, 0, 1, 2)

# Estiramiento
layout_grid.setColumnStretch(0, 1)
layout_grid.setColumnStretch(1, 2)

# ============================================================================
# WIDGETS CONTENEDOR
# ============================================================================

# -------------------------------------------------------------------
# QWidget - Widget base (padre de todos los widgets)
# -------------------------------------------------------------------
"""
widget = QWidget(parent=None)
#
# Es la clase base de todos los widgets visuales en Qt.
#
# Métodos principales:
#   setLayout(layout)           -> Establece layout
#   layout()                    -> Devuelve layout
#   setParent(parent)          -> Establece padre
#   parentWidget()            -> Devuelve widget padre
#   setWindowTitle(title)      -> Título
#   windowTitle()              -> Devuelve título
#   setWindowIcon(icon)        -> Icono
#   setGeometry(x, y, w, h)    -> Posición y tamaño
#   geometry()                  -> Devuelve QRect con posición y tamaño
#   x(), y()                    -> Posición
#   width(), height()           -> Tamaño
#   setFixedSize(w, h)          -> Tamaño fijo
#   setFixedWidth(w)           -> Ancho fijo
#   setFixedHeight(h)          -> Alto fijo
#   setMinimumSize(w, h)        -> Tamaño mínimo
#   setMaximumSize(w, h)        -> Tamaño máximo
#   setEnabled(bool)           -> Habilita/deshabilita
#   isEnabled()                -> Devuelve si está habilitado
#   setVisible(bool)           -> Muestra/oculta
#   isVisible()                -> Devuelve si es visible
#   show()                      -> Muestra widget
#   hide()                      -> Oculta widget
#   close()                     -> Cierra widget
#   raise_()                    -> Trae al frente
#   lower()                     -> Manda atrás
#   update()                    -> Solicita repintado
#   repaint()                   -> Repinta inmediatamente
#   setStyleSheet(stylesheet)  -> CSS
#   setToolTip(text)           -> Tooltip
#   toolTip()                   -> Devuelve tooltip
#   setFocus()                  -> Da foco
#   hasFocus()                 -> Devuelve si tiene foco
#   setFocusPolicy(policy)    -> Política de foco:
#                                   Qt.NoFocus
#                                   Qt.TabFocus
#                                   Qt.ClickFocus
#                                   Qt.StrongFocus
#                                   Qt.WheelFocus
#   focusPolicy()              -> Devuelve política
#   setCursor(cursor)          -> Cursor del ratón:
#                                   Qt.ArrowCursor
#                                   Qt.PointingHandCursor
#                                   Qt.CrossCursor
#                                   Qt.IBeamCursor
#                                   Etc.
#   setAutoFillBackground(bool) -> Relleno automático de fondo
#   setBackgroundRole(role)    -> Rol de fondo:
#                                   QPalette.Window
#                                   QPalette.Base
#                                   QPalette.AlternateBase
#   setForegroundRole(role)    -> Rol de primer plano:
#                                   QPalette.WindowText
#                                   QPalette.Text
#   palette()                  -> Devuelve paleta
#   setPalette(palette)        -> Establece paleta
#   font()                      -> Devuelve fuente
#   setFont(font)              -> Establece fuente
#   setWindowFlags(flags)      -> Flags de ventana:
#                                   Qt.Widget
#                                   Qt.Window
#                                   Qt.Dialog
#                                   Qt.Sheet
#                                   Qt.Popup
#                                   Qt.Tool
#                                   Qt.ToolTip
#                                   Qt.WindowStaysOnTopHint
#                                   Qt.FramelessWindowHint
#                                   Qt.WindowTitleHint
#                                   Qt.WindowSystemMenuHint
#                                   Qt.WindowMinimizeButtonHint
#                                   Qt.WindowMaximizeButtonHint
#                                   Qt.WindowCloseButtonHint
#                                   Qt.WindowContextHelpButtonHint
#                                   Qt.WindowMinMaxButtonsHint
#                                   Qt.SubWindow
#
# Señales:
#   destroyed(QObject*)        -> Widget destruido
#   objectNameChanged(const QString&) -> Nombre cambió
#
# Eventos (override):
#   paintEvent(event)          -> Pintar widget
#   resizeEvent(event)         -> Redimensionar
#   mousePressEvent(event)     -> Click de ratón
#   mouseReleaseEvent(event)   -> Soltar botón
#   mouseMoveEvent(event)      -> Mover ratón
#   mouseDoubleClickEvent(event) -> Doble click
#   wheelEvent(event)           -> Rueda del ratón
#   keyPressEvent(event)       -> Tecla presionada
#   keyReleaseEvent(event)     -> Tecla soltada
#   focusInEvent(event)        -> Gana foco
#   focusOutEvent(event)       -> Pierde foco
#   enterEvent(event)          -> Ratón entra
#   leaveEvent(event)          -> Ratón sale
#   closeEvent(event)          -> Cerrar widget
#   showEvent(event)           -> Mostrar widget
#   hideEvent(event)           -> Ocultar widget
"""
widget = QWidget()
widget.setStyleSheet("background-color: lightgray;")
widget.setFixedSize(300, 200)

# ============================================================================
# GRÁFICOS E IMÁGENES
# ============================================================================

# -------------------------------------------------------------------
# QPixmap - Imagen (óptima para displaying)
# -------------------------------------------------------------------
"""
pixmap = QPixmap(file_path)
# o
pixmap = QPixmap(width, height)  # Crear pixmap vacío
#
# Métodos principales:
#   load(file_path)            -> Carga imagen desde archivo
#   loadFromData(data)        -> Carga desde bytes
#   save(file_path, format=None, quality=-1) -> Guarda imagen
#   width()                    -> Ancho
#   height()                   -> Alto
#   size()                     -> Tamaño (QSize)
#   isNull()                   -> Devuelve si es nulo/vacío
#   scaled(width, height, aspectMode=Qt.IgnoreAspectRatio, mode=Qt.FastTransformation)
#       -> Escala imagen
#       aspectMode: Qt.IgnoreAspectRatio, Qt.KeepAspectRatio, Qt.KeepAspectRatioByExpanding
#       mode: Qt.FastTransformation, Qt.SmoothTransformation
#   scaledToWidth(width, mode=Qt.FastTransformation)
#   scaledToHeight(height, mode=Qt.FastTransformation)
#   scaledToHeight(height, mode=Qt.SmoothTransformation)
#   copy(rect=None)           -> Copia región (por defecto toda la imagen)
#   fill(color=Qt.white)       -> Rellena con color
#   setMask(bmpMask)          -> Máscara de bits
#   mask()                     -> Devuelve máscara
#   hasAlpha()                 -> Tiene canal alpha
#   hasAlphaChannel()          -> Tiene canal alpha (más preciso)
#   createHeuristicMask(clipped=True) -> Crea máscara heurística
#   createMaskFromColor(color, mode=Qt.MaskInColor)
#       -> Crea máscara desde color
"""
pixmap = QPixmap("imagen.png")
pixmap_scaled = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)

# -------------------------------------------------------------------
# QIcon - Icono (para botones, acciones, etc.)
# -------------------------------------------------------------------
"""
icon = QIcon(file_path)
# o
icon = QIcon(pixmap)
# o
icon = QIcon()  # Icono vacío
#
# Métodos principales:
#   addFile(file_path, size=QSize(), mode=QIcon.Normal, state=QIcon.Off)
#       -> Añade archivo al icono (para diferentes tamaños/estados)
#   addPixmap(pixmap, mode=QIcon.Normal, state=QIcon.Off)
#       -> Añade pixmap
#   pixmap(size, mode=Normal, state=Off)
#       -> Devuelve pixmap del tamaño indicado
#   availableSizes(mode, state) -> Tamaños disponibles
#   actualSize(mode, state)    -> Tamaño real usado
#   isNull()                   -> Devuelve si es nulo
#   isDetachable()            -> Se puede separar
#   setDetachAttachment(bool)  -> Establece si es separable
#   swap(other)               -> Intercambia iconos
#   cacheKey()                -> Clave de caché
#
# Modos de icono:
#   QIcon.Normal (normal)
#   QIcon.Disabled (deshabilitado)
#   QIcon.Active (activo)
#   QIcon.Selected (seleccionado)
#
# Estados:
#   QIcon.On (encendido/activo)
#   QIcon.Off (apagado/inactivo)
"""
icon = QIcon("icono.png")

# -------------------------------------------------------------------
# QPalette - Paleta de colores
# -------------------------------------------------------------------
"""
palette = QPalette()
# o
palette = QPalette(color)
# o
palette = QPalette(color, role)
#
# Métodos principales:
#   setColor(role, color)      -> Establece color para rol
#   setBrush(role, brush)      -> Establece brush (pincel) para rol
#   color(role)                -> Devuelve color de rol
#   brush(role)               -> Devuelve brush de rol
#   isCopyOf(other)            -> Es copia de otra paleta
#   resolve(other)            -> Combina paletas
#   setColorGroup(group, foreground, background, button, etc.)
#       -> Establece grupo de colores
#
# Roles de color:
#   QPalette.Window (fondo general)
#   QPalette.WindowText (texto general)
#   QPalette.Base (fondo de widgets de entrada)
#   QPalette.AlternateBase (base alternativa para listas)
#   QPalette.ToolTipBase (fondo de tooltip)
#   QPalette.ToolTipText (texto de tooltip)
#   QPalette.Text (texto)
#   QPalette.Button (fondo de botón)
#   QPalette.ButtonText (texto de botón)
#   QPalette.BrightText (texto brillante)
#   QPalette.Highlight (selección)
#   QPalette.HighlightedText (texto seleccionado)
#   QPalette.Link (enlace)
#   QPalette.LinkVisited (enlace visitado)
#   QPalette.PlaceholderText (placeholder)
#   QPalette.Shadow
#   QPalette.Light
#   QPalette.Midlight
#   QPalette.Dark
#   QPalette.Mid
#   QPalette.Dark
#   QPalette.Shadow
#   QPalette.PlaceholderText
#
# Roles de brush (para texturas):
#   QPalette.WindowText
#   QPalette.Background
#   QPalette.AlternateBase
#   QPalette.ToolTipBase
#   QPalette.ToolTipText
#   QPalette.Text
#   QPalette.Button
#   QPalette.BrightText
#   QPalette.Highlight
#   QPalette.HighlightedText
"""
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor("lightblue"))
widget.setPalette(palette)

# -------------------------------------------------------------------
# QColor - Color
# -------------------------------------------------------------------
"""
color = QColor(name)
# Formatos:
#   QColor("#RRGGBB") o QColor("#RGB")
#   QColor("nombre")  # nombres CSS: "red", "blue", "lightgray", etc.
#   QColor(r, g, b)   # RGB
#   QColor(r, g, b, a) # RGBA (a = alpha, 0-255)
#   QColor(color_spec) # cadena "rgba(r,g,b,a)"
#
# Métodos principales:
#   red(), green(), blue(), alpha() -> Componentes
#   setRed(r), setGreen(g), setBlue(b), setAlpha(a)
#   name()                     -> Nombre (#RRGGBB)
#   setNamedColor(name)        -> Establece desde nombre
#   isValid()                  -> Color válido
#   lighter(factor=150)       -> Color más claro
#   darker(factor=150)         -> Color más oscuro
#   light()                   -> Color claro
#   dark()                     -> Color oscuro
#   spec()                     -> Tipo de color (Rgb, Hsv, etc.)
#   toRgb()                   -> Convierte a QRgb
#   toHsv()                   -> Convierte a QHsv
#   getRgb()                  -> Tupla (r, g, b)
#   getHsv()                  -> Tupla (h, s, v)
"""
color = QColor("lightblue")
color.setRed(255)
color.setGreen(0)
color.setBlue(0)

# -------------------------------------------------------------------
# QFont - Fuente
# -------------------------------------------------------------------
"""
font = QFont()
# o
font = QFont(family, size=-1, weight=-1, italic=False)
#
# Constructores:
#   family: nombre de familia ("Arial", "Times", "Courier")
#   size: tamaño en puntos (-1 = por defecto)
#   weight: peso (QFont.Normal=50, QFont.Bold=75)
#   italic: cursiva
#
# Métodos principales:
#   setFamily(family)          -> Establece familia
#   family()                   -> Devuelve familia
#   setPointSize(size)         -> Tamaño en puntos
#   setPointSizeF(size)        -> Tamaño en puntos con decimales
#   pointSize()                -> Devuelve tamaño en puntos
#   pointSizeF()               -> Devuelve tamaño en puntos (float)
#   setPixelSize(size)         -> Tamaño en píxeles
#   pixelSize()                -> Devuelve tamaño en píxeles
#   setBold(bool)              -> Negrita
#   bold()                      -> Devuelve si es negrita
#   setItalic(bool)            -> Cursiva
#   italic()                   -> Devuelve si es cursiva
#   setUnderline(bool)         -> Subrayado
#   underline()                -> Devuelve si tiene subrayado
#   setStrikeOut(bool)         -> Tachado
#   strikeOut()                -> Devuelve si tiene tachado
#   setWeight(weight)         -> Peso (0-100)
#   weight()                   -> Devuelve peso
#   setStyle(style)            -> Estilo:
#                                   QFont.StyleNormal
#                                   QFont.StyleItalic
#                                   QFont.StyleOblique
#   style()                    -> Devuelve estilo
#   setStyleHint(hint)         -> Hint de estilo:
#                                   QFont.SansSerif
#                                   QFont.Serif
#                                   QFont.Monospace
#                                   QFont.Courier
#                                   QFont.AnyStyle
#                                   QFont.Helvetica
#   styleHint()                -> Devuelve hint
#   setKerning(bool)           -> Kerning
#   kerning()                  -> Devuelve si hay kerning
#   setLetterSpacing(type, spacing) -> Espaciado de letras
#   letterSpacing()            -> Devuelve espaciado
#   setWordSpacing(spacing)    -> Espaciado de palabras
#   wordSpacing()              -> Devuelve espaciado
"""
font = QFont("Arial", 16)
font.setBold(True)
font.setUnderline(True)

# -------------------------------------------------------------------
# QKeySequence - Secuencia de teclas
# -------------------------------------------------------------------
"""
shortcut = QKeySequence("Ctrl+S")
# o
shortcut = QKeySequence(key, key, ...)
# o
shortcut = QKeySequence.fromString("Ctrl+S")
#
# Formatos:
#   "Ctrl+S" - texto estándar
#   Qt.CTRL + Qt.Key_S - constantes Qt
#
# Métodos principales:
#   toString()                 -> Convierte a string
#   count()                    -> Número de teclas en secuencia
#   isEmpty()                  -> Vacía
#   matches(other)             -> Compara con otra secuencia
#
# Constantes de modificación:
#   Qt.CTRL, Qt.SHIFT, Qt.ALT, Qt.META (Super/Windows)
#
# Teclas comunes:
#   Qt.Key_S, Qt.Key_A, Qt.Key_1
#   Qt.Key_Return, Qt.Key_Enter
#   Qt.Key_Space, Qt.Key_Tab, Qt.Key_Backspace
#   Qt.Key_Delete, Qt.Key_Insert
#   Qt.Key_Home, Qt.Key_End, Qt.Key_PageUp, Qt.Key_PageDown
#   Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right
#   Qt.Key_F1 ... Qt.Key_F12
#   Qt.Key_Escape
"""
shortcut = QKeySequence("Ctrl+O")
action.setShortcut(shortcut)

# ============================================================================
# MODELOS DE DATOS (Model-View)
# ============================================================================

# -------------------------------------------------------------------
# QStandardItemModel - Modelo de items estándar
# -------------------------------------------------------------------
"""
model = QStandardItemModel(rows=0, columns=0, parent=None)
#
# Constructor:
#   rows: número inicial de filas
#   columns: número inicial de columnas
#   parent: widget padre
#
# Métodos principales:
#   setRowCount(rows)          -> Establece número de filas
#   rowCount()                  -> Devuelve número de filas
#   setColumnCount(columns)    -> Establece número de columnas
#   columnCount()              -> Devuelve número de columnas
#   setItem(row, column, item) -> Establece item en celda
#   setItem(row, item)         -> Establece item en fila (primera columna)
#   item(row, column=0)        -> Devuelve item
#   takeItem(row, column=0)    -> Elimina y devuelve item
#   takeRow(row)               -> Elimina fila
#   takeColumn(column)         -> Elimina columna
#   clear()                     -> Limpia todos los items
#   clearItemData()            -> Limpia datos (roles)
#   insertRow(row, items=None) -> Inserta fila
#   insertRows(row, count)     -> Inserta filas
#   insertColumn(column, items=None) -> Inserta columna
#   insertColumns(column, count) -> Inserta columnas
#   removeRow(row)             -> Elimina fila
#   removeRows(row, count)     -> Elimina varias filas
#   removeColumn(column)       -> Elimina columna
#   removeColumns(column, count) -> Elimina varias columnas
#   setHorizontalHeaderLabels(labels) -> Labels de encabezado horizontal
#   setVerticalHeaderLabels(labels)   -> Labels de encabezado vertical
#   sort(column, order=Qt.AscendingOrder) -> Ordena por columna
#
# Señales:
#   dataChanged(topLeft, bottomRight, roles) -> Datos cambiaron
#   headerDataChanged(orientation, first, last) -> Header cambió
#   layoutChanged()             -> Layout cambió
#   layoutAboutToBeChanged()    -> Layout va a cambiar
#   rowsInserted(parent, first, last) -> Filas insertadas
#   rowsRemoved(parent, first, last) -> Filas eliminadas
#   columnsInserted(parent, first, last) -> Columnas insertadas
#   columnsRemoved(parent, first, last) -> Columnas eliminadas
"""
model = QStandardItemModel(0, 3)  # 0 filas, 3 columnas
model.setHorizontalHeaderLabels(["Nombre", "Precio", "Cantidad"])

# Añadir fila
row = []
row.append(QStandardItem("Manzana"))
row.append(QStandardItem("1.50"))
row.append(QStandardItem("10"))
model.appendRow(row)

# -------------------------------------------------------------------
# QStandardItem - Item individual para el modelo
# -------------------------------------------------------------------
"""
item = QStandardItem(text="")
# o
item = QStandardItem(icon, text)
#
# Constructores:
#   - text: texto del item
#   - icon: icono opcional
#
# Métodos principales:
#   setText(text)              -> Establece texto
#   text()                      -> Devuelve texto
#   setIcon(icon)              -> Establece icono
#   icon()                      -> Devuelve icono
#   setData(data, role=Qt.UserRole) -> Establece dato
#   data(role=Qt.UserRole)      -> Devuelve dato
#   setEditable(bool)          -> Editable
#   isEditable()               -> Devuelve si es editable
#   setCheckable(bool)         -> Con checkbox
#   setCheckState(state)       -> Estado: Qt.Checked, Qt.Unchecked
#   checkState()              -> Devuelve estado
#   setStatusTip(tip)          -> Tooltip de estado
#   setToolTip(tip)            -> Tooltip
#   setFont(font)              -> Fuente
#   setBackground(color)       -> Color de fondo
#   setForeground(color)       -> Color de texto
#   setFlags(flags)            -> Flags de item:
#                                   Qt.ItemIsEnabled
#                                   Qt.ItemIsSelectable
#                                   Qt.ItemIsEditable
#                                   Qt.ItemIsDragEnabled
#                                   Qt.ItemIsDropEnabled
#                                   Qt.ItemIsUserCheckable
#                                   Combinar con |
#   appendRow(items)           -> Añade fila de items hijos
#   insertRow(row, items)      -> Inserta fila
#   insertColumn(column)       -> Inserta columna
#   takeRow(row)               -> Elimina fila
#   child(row, column=0)       -> Devuelve hijo
#   parent()                   -> Devuelve padre
#   row()                      -> Índice de fila
#   column()                   -> Índice de columna
#   model()                    -> Devuelve modelo
"""
item = QStandardItem("Elemento")
item.setCheckable(True)
item.setData(123)  # Datos personalizados
item.setEditable(False)

# ============================================================================
# CONSTANTES DE QT (Qt)
# ============================================================================

"""
Qt contiene muchas constantes útiles para configuraciones.
"""

# Alineación
# Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignJustify
# Qt.AlignTop, Qt.AlignBottom, Qt.AlignVCenter
# Qt.AlignCenter = AlignHCenter | AlignVCenter

# Orientación
# Qt.Horizontal, Qt.Vertical

# Modificadores de teclado
# Qt.CTRL, Qt.SHIFT, Qt.ALT, Qt.META, Qt.KeypadModifier

# Orientación de tabs
# QTabWidget.North, South, West, East

# Bordes y esquinas
# Qt.NoPen, Qt.SolidPen, Qt.DashLine, etc.
# Qt.RoundCorner, etc.

# Estados
# Qt.Checked, Qt.Unchecked, Qt.PartiallyChecked

# Focus
# Qt.TabFocus, Qt.ClickFocus, Qt.StrongFocus, Qt.NoFocus

# Mouse buttons
# Qt.LeftButton, Qt.RightButton, Qt.MidButton

# ============================================================================
# CONFIGURACIÓN FINAL DE LA APLICACIÓN
# ============================================================================

window = QMainWindow()
window.setWindowTitle("Mi App")
window.setFixedSize(800, 600)

widget = QWidget()
window.setCentralWidget(widget)

layout = QVBoxLayout()
widget.setLayout(layout)

app = QApplication(sys.argv)
window.show()
app.exec()