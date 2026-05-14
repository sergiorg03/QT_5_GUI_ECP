# RESUMEN EXAMEN - Interfaces Gráficas (PyQt5 + Pygame Zero)

---

## 1. ESTRUCTURA BÁSICA DE UNA APP PyQt5

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(ancho, alto)
        # widgets y lógica aquí
        self.setCentralWidget(QWidget())

app = QApplication(sys.argv)
window = MainWindow("Mi App")
window.show()
app.exec()
```

**Flujo:** `QApplication` → `MainWindow(QMainWindow)` → `show()` → `app.exec()`.

---

## 2. WIDGETS PRINCIPALES (PyQt5)

| Widget | Descripción | Import |
|--------|-------------|--------|
| `QMainWindow` | Ventana principal con menú, toolbar, statusbar | `QMainWindow` |
| `QWidget` | Widget genérico/contenedor | `QWidget` |
| `QPushButton` | Botón clickeable | `QPushButton` |
| `QLabel` | Etiqueta de texto o imagen | `QLabel` |
| `QLineEdit` | Campo de texto de una línea | `QLineEdit` |
| `QTextEdit` | Área de texto multilínea | `QTextEdit` |
| `QCheckBox` | Casilla de verificación | `QCheckBox` |
| `QRadioButton` | Botón de opción | `QRadioButton` |
| `QComboBox` | Lista desplegable | `QComboBox` |
| `QSpinBox` / `QDoubleSpinBox` | Selector numérico | `QSpinBox` / `QDoubleSpinBox` |
| `QSlider` | Deslizador | `QSlider` |
| `QProgressBar` | Barra de progreso | `QProgressBar` |
| `QLCDNumber` | Display tipo LCD | `QLCDNumber` |
| `QDial` | Dial giratorio | `QDial` |
| `QDateEdit` / `QTimeEdit` / `QDateTimeEdit` | Selector fecha/hora | `QDateEdit` / `QTimeEdit` / `QDateTimeEdit` |
| `QFontComboBox` | Selector de fuentes | `QFontComboBox` |
| `QTabWidget` | Pestañas | `QTabWidget` |
| `QTableView` | Tabla de datos | `QTableView` |
| `QListWidget` | Lista | `QListWidget` |

---

## 3. SEÑALES Y SLOTS (Eventos)

### Botón
```python
button = QPushButton("Texto")
button.clicked.connect(self.mi_funcion)     # click completo
button.released.connect(self.mi_funcion)    # al soltar
button.clicked.connect(self.funcion_con_checked)  # si es checkeable
```

### Campo de texto (QLineEdit)
```python
self.input = QLineEdit("placeholder")
self.input.textChanged.connect(self.mi_funcion)
self.input.textChanged.connect(self.label.setText)  # atajo directo
```

### Señales más comunes
| Señal | Widget | Cuándo se dispara |
|-------|--------|-------------------|
| `clicked` | QPushButton | Al hacer click |
| `released` | QPushButton | Al soltar el botón |
| `textChanged` | QLineEdit | Cambia el texto |
| `currentIndexChanged` | QComboBox | Cambia selección |
| `valueChanged` | QSpinBox/QSlider | Cambia el valor |
| `triggered` | QAction | Se ejecuta una acción de menú |

---

## 4. EVENTOS DE RATÓN

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # Activar seguimiento ratón

    def mouseMoveEvent(self, event):
        print(event.globalPos())     # Posición global
        # event.x(), event.y()       # Posición local
        # event.button()             # Botón pulsado
        # event.buttons()            # Máscara de botones

    def mousePressEvent(self, event):
        print(f"Botón: {event.button()}")

    def mouseReleaseEvent(self, event):
        print("Ratón liberado")

    def mouseDoubleClickEvent(self, event):
        print("Doble click")
```

**Máscaras de botón:**
- `Qt.LeftButton` → 001
- `Qt.RightButton` → 010
- `Qt.MiddleButton` → 100
- `event.buttons()` → combinación (111 = todos)

---

## 5. MENÚS Y BARRAS

### Barra de herramientas (QToolBar)
```python
toolbar = QToolBar("Nombre")
toolbar.setIconSize(QSize(32, 32))
toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

accion = QAction(QIcon("icono.png"), "Texto", self)
accion.setStatusTip("Descripción")
accion.triggered.connect(lambda: self.funcion("dato"))
toolbar.addAction(accion)

self.addToolBar(toolbar)
self.setStatusBar(QStatusBar(self))
```

### Menú clásico (menuBar)
```python
menu = self.menuBar()
file_menu = menu.addMenu("&Fichero")   # &F = atajo Alt+F

accion = QAction(QIcon("icono.png"), "&Abrir...", self)
accion.setStatusTip("Abrir archivo")
accion.setShortcut(QKeySequence("Ctrl+Q"))  # Atajo teclado
accion.triggered.connect(lambda: self.handler("Abrir"))
file_menu.addAction(accion)

file_menu.addSeparator()  # Línea separadora

# Submenú
submenu = file_menu.addMenu("&Submenu")
submenu.addAction(otra_accion)
```

### Menú contextual
```python
# Opción 1: Evento contextMenuEvent
def contextMenuEvent(self, event):
    menu = QMenu(self)
    menu.addAction(QAction("Opción 1", self))
    menu.exec_(event.globalPos())

# Opción 2: Custom (más control)
self.setContextMenuPolicy(Qt.CustomContextMenu)
self.customContextMenuRequested.connect(self.on_context_menu)

def on_context_menu(self, pos):
    menu = QMenu(self)
    menu.addAction(QAction("Opción", self))
    menu.exec_(self.mapToGlobal(pos))
```

---

## 6. LAYOUTS (Diseños)

| Layout | Clase | Comportamiento |
|--------|-------|----------------|
| **Vertical** | `QVBoxLayout()` | Widgets apilados verticalmente |
| **Horizontal** | `QHBoxLayout()` | Widgets en fila horizontal |
| **Cuadrícula** | `QGridLayout()` | Widgets en filas y columnas |
| **Apilado** | `QStackedLayout()` | Un widget visible por vez (como pestañas) |
| **Pestañas** | `QTabWidget()` | Pestañas nativas |

```python
# Vertical
layout = QVBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)

# Horizontal
layout = QHBoxLayout()
layout.addWidget(widget1)

# Grid (fila, columna)
layout = QGridLayout()
layout.addWidget(widget, 0, 1)  # fila 0, columna 1

# Stacked (índice)
layout = QStackedLayout()
layout.addWidget(pagina1)
layout.setCurrentIndex(0)  # Muestra la página 0

# Tabs
tabs = QTabWidget()
tabs.setTabPosition(QTabWidget.West)  # Posición de pestañas
tabs.setMovable(True)
tabs.addTab(widget, "Nombre Pestaña")

# Layouts anidados
layout_principal = QVBoxLayout()
layout_fila = QHBoxLayout()
layout_fila.addWidget(...)
layout_principal.addLayout(layout_fila)  # ¡addLayout! no addWidget

# Asignar layout a la ventana
widget = QWidget()
widget.setLayout(layout)
self.setCentralWidget(widget)
```

---

## 7. DIÁLOGOS (QMessageBox, QFileDialog)

### QMessageBox
```python
dialog = QMessageBox(self)
dialog.setWindowTitle("Título")
dialog.setText("Mensaje")
dialog.setIcon(QMessageBox.Question)  # Question, Information, Warning, Critical
dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
button = dialog.exec()
if button == QMessageBox.Yes:
    # hacer algo
```

### QFileDialog
```python
# Abrir archivo
dialog = QFileDialog(self)
dialog.setFileMode(QFileDialog.ExistingFiles)
dialog.setNameFilter("Textos (*.txt);;Todos (*.*)")
if dialog.exec():
    ruta = dialog.selectedFiles()[0]

# Guardar archivo
dialog = QFileDialog(self)
dialog.setAcceptMode(QFileDialog.AcceptSave)
dialog.setNameFilter("Textos (*.txt)")
if dialog.exec():
    ruta = dialog.selectedFiles()[0]
```

### Leer/Escribir archivos
```python
def open_file(self, ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def save_file(self, ruta, contenido):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
```

---

## 8. WIDGETS PERSONALIZADOS

```python
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QWidget, QLabel

# Widget con color de fondo
class CustomColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

# Label con color + texto centrado
class CustomColorLabel(QLabel):
    def __init__(self, color, text):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        self.setText(text)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)
```

---

## 9. MODELO_QMainWindow (Plantilla)

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        # Su código aquí
        # Fin de bloque de código
        self.setCentralWidget(QWidget())

app = QApplication(sys.argv)
window = MainWindow("My App")
window.show()
app.exec()
```

---

## 10. TABLAS CON QTableView + QStandardItemModel

```python
from PyQt5.QtGui import QStandardItemModel, QStandardItem

self.model = QStandardItemModel(0, 2, self)  # 0 filas, 2 columnas
self.model.setHorizontalHeaderLabels(["Col1", "Col2"])

self.tabla = QTableView()
self.tabla.setModel(self.model)
self.tabla.verticalHeader().setVisible(False)        # Ocultar numeración
self.tabla.horizontalHeader().setStretchLastSection(True)
self.tabla.setEditTriggers(QTableView.NoEditTriggers) # No editable

# Añadir filas
item_col1 = QStandardItem("valor")
item_col1.setTextAlignment(Qt.AlignCenter)
item_col2 = QStandardItem("123")
self.model.appendRow([item_col1, item_col2])

# Limpiar
self.model.setRowCount(0)
```

---

## 11. PYGAME ZERO (primerWidget.py)

Librería para GUI con ciclo `update()` / `draw()`.

### Ciclo de vida
```python
import pgzrun

WIDTH = 720
HEIGHT = 480

def update():
    # Lógica (física, colisiones, etc.)
    pass

def draw():
    # Dibujar en pantalla
    screen.clear()
    screen.draw.text("Texto", (10, 10), color="white", fontsize=20)

pgzrun.go()
```

### Eventos en Pygame Zero
```python
def on_mouse_move(pos):
    # pos = (x, y)
    pass

def on_mouse_down(pos, button):
    pass

def on_mouse_up(pos, button):
    pass

def on_key_down(key, mod, unicode):
    # key = pygame.K_TAB, K_RETURN, K_BACKSPACE, etc.
    pass

def on_key_up(key, mod):
    pass
```

### Dibujar formas
```python
screen.draw.rect(rect, color)           # borde
screen.draw.filled_rect(rect, color)     # relleno
screen.draw.text("texto", center=(x, y), color="white", fontsize=20)
screen.draw.line((x1,y1), (x2,y2), color)
screen.blit("imagen", (x, y))           # dibujar imagen/textura
```

### Colores comunes (RGB)
```python
RED = (255, 0, 0); GREEN = (0, 255, 0); BLUE = (0, 0, 255)
WHITE = (255, 255, 255); BLACK = (0, 0, 0); GRAY = (128, 128, 128)
```

### Clase Window propia (primerWidget.py)
- **`Window`**: contiene lista de controles, gestiona eventos y los delega a cada control.
- **`Widget`** (clase base): con `pos`, `size`, `active`, métodos `update()`, `draw()`, `on_mouse_move`, `on_click`, `on_key_down`.
- **`Button`**: Rect con texto, colores por estado (hover/clicked/normal), callback `on_click_callback`.
- **`Label`**: muestra texto en posición.
- **`InputText`**: campo editable con cursor parpadeante, placeholder, maneja teclas (BACKSPACE, caracteres).
- **`CheckBox`**: cuadrado checkeable con tick dibujado con `pygame.draw.lines()`.
- **`StatusBar`**: barra inferior que muestra coordenadas del ratón y control activo.
- **Focus con TAB**: `Window.activate_control(None)` cicla al siguiente control.
- **Enter en botón**: si el control activo es un `Button` o `CheckBox`, se ejecuta `on_click`.

---

## 12. PONG (Pygame Zero) - ESTRUCTURA

### Clases principales
- **`Game`**: orquestador, contiene `bats[2]`, `ball`, `impact[]`. Métodos `update()` y `draw()`.
- **`Bat(Actor)`**: paleta. Se mueve con función `move_func` (jugador o IA). `ai()` calcula movimiento hacia la pelota.
- **`Ball(Actor)`**: pelota con velocidad `dx, dy` normalizada. Detecta colisiones con bordes y paletas. Incrementa velocidad al golpear.
- **`Impact(Actor)`**: efecto visual al golpear (animación de frames).

### Máquina de estados
```python
class State(Enum):
    MENU = 1
    PLAY = 2
    GAME_OVER = 3
```

### Controles
- Jugador 1: `W` / `S`
- Jugador 2: `UP` / `DOWN`
- Espacio: iniciar/continuar
- Menú: `UP`/`DOWN` para cambiar número de jugadores

### Fórmulas útiles
- **Normalizar vector**: `math.hypot(x, y)` → dividir componentes por la longitud
- **Limitar valor**: `min(max_val, max(min_val, valor))`
- **Colisión**: diferencia de posición dentro de rango (`difference_y > -64 and difference_y < 64`)

---

## 13. TIPS Y TRUCOS PARA EL EXAMEN

1. **Siempre** llamar a `super().__init__()` en el constructor.
2. `setCentralWidget()` acepta UN widget. Para múltiples, usar un layout dentro de un `QWidget`.
3. Los layouts anidados se añaden con `addLayout()`, los widgets con `addWidget()`.
4. `setFixedSize()` evita redimensionar la ventana.
5. Para que un widget hijo aparezca en posición específica, pasar `self` como padre o usar `move(x, y)`.
6. Los botones pueden ser `checkable` → emiten `clicked(bool)`.
7. `setDisabled(True)` / `setEnabled(False)` desactiva widgets.
8. `QMainWindow` ya viene con `menuBar()` y `statusBar()` incorporados.
9. `mapToGlobal(pos)` convierte coordenadas locales a globales (útil en menús contextuales).
10. Pygame Zero usa `screen`, `keyboard`, `mouse` como objetos globales.
11. `Actor` de Pygame Zero es un sprite con `x, y, pos, image` y métodos `draw()`, `update()`.
