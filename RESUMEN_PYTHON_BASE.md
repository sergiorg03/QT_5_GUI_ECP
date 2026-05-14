# RESUMEN REPASO - Python Base (Estructuras de Control)

---

## 1. OPERADORES

### Ternario

```python
"Par" if n % 2 == 0 else "Impar"
```

### Lógicos

```python
and  # True si ambas condiciones True
or   # True si al menos una True
not  # Niega la condición
```

### Identidad vs Igualdad

```python
x is y    # ¿Mismo objeto en memoria?
x == y    # ¿Mismos valores?
```

### Pertenencia

```python
"a" in "hola"     # True
5 not in [1,2,3]  # True
```

### Asignación compuesta

```python
x += 2   # x = x + 2
x -= 2   # x = x - 2
x *= 2   # x = x * 2
```

### Bitwise

```python
&   # AND binario
|   # OR binario
^   # XOR binario
<<  # Desplazar izquierda (multiplica por 2^n)
>>  # Desplazar derecha (divide por 2^n)
```

### Prioridad

`**` > `* / // %` > `+ -` > comparaciones > `not` > `and` > `or`

---

## 2. CONVERSIÓN DE TIPOS

```python
int(x)      # "5" → 5, 5.7 → 5 (trunca)
float(x)    # "5.5" → 5.5, 5 → 5.0
str(x)      # 5 → "5", [1,2] → "[1, 2]"
list(x)     # "hola" → ['h','o','l','a']
tuple(x)    # [1,2] → (1,2)
set(x)      # [1,1,2] → {1,2} (elimina duplicados)
complex(x,y)# (5.7+0j)
```

**Cuidado:** `int("Hola")` → **ValueError**

---

## 3. ESTRUCTURAS DE CONTROL

### if / elif / else

```python
if condicion:
    pass
elif otra:
    pass
else:
    pass
```

### match-case (Python 3.10+)

```python
match valor:
    case 1 | 2 | 12:
        print("Invierno")
    case _:
        print("Otro")  # wildcard = default
```

### match con tuplas

```python
match (x, y):
    case (0, 0): print("Origen")
    case (x, 0): print("Eje X")
    case (0, y): print("Eje Y")
    case _: print("Otro")
```

### for

```python
for i in range(5):        # 0,1,2,3,4
for i in range(1, 5):     # 1,2,3,4
for i in range(0, 10, 2): # 0,2,4,6,8
for c in "Python":
for item in lista:
```

### while

```python
while condicion:
    pass

while True:   # bucle infinito (romper con break)
    pass
```

### break / continue / else en bucles

```python
for i in range(10):
    if i == 5:
        break        # sale del bucle
    if i % 2 == 0:
        continue     # salta a siguiente iteración
else:
    # se ejecuta SOLO si NO hubo break
    pass
```

### Slicing [inicio:fin:paso]

```python
cadena = "Python"
cadena[0:2]    # "Py"
cadena[:]      # copia completa
cadena[::-1]   # invertir → "nohtyP"
cadena[::2]    # caracteres pares → "Pto"
cadena[:-1]    # "Pytho"
```

### Comprensión de listas

```python
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(10) if x % 2 == 0]
```

---

## 4. FUNCIONES

```python
def suma(a, b=2):          # valor por defecto
    return a + b

def args(*args, **kwargs): # *args = tupla, **kwargs = dict
    pass

# Lambda
z = lambda a, b: a + b
z(1, 2)  # 3
```

### Anotaciones (Type Hints)

```python
def suma(n1: float, n2: float) -> float:
    return n1 + n2

print(suma.__annotations__)  # {'n1': float, 'n2': float, 'return': float}
```

### Paso por valor/referencia

- **Inmutables** (int, str, tuple): se pasa copia
- **Mutables** (list, dict, set): se pasa referencia (se modifica el original)

---

## 5. DECORADORES

```python
from functools import wraps

def decorador(func):
    @wraps(func)           # preserva metadatos (nombre, docstring)
    def wrapper(*args, **kwargs):
        # código antes
        res = func(*args, **kwargs)
        # código después
        return res
    return wrapper

@decorador
def mi_funcion():
    pass
# Equivale a: mi_funcion = decorador(mi_funcion)
```

### Decorador parametrizado (3 niveles)

```python
def reintentar(intentos):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(intentos):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == intentos - 1: raise e
        return wrapper
    return decorator

@reintentar(intentos=3)
def conectar(url):
    pass
```

### Decorador @log (loguear a fichero)

```python
@log("fichero.txt")
def suma(a, b):
    return a + b
```

---

## 6. EXCEPCIONES

```python
try:
    codigo_riesgoso
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Error múltiple")
else:
    # Solo si NO hubo excepción
finally:
    # Siempre se ejecuta (liberar recursos)

raise ZeroDivisionError("Mensaje")
```

### Excepción personalizada

```python
class MiError(Exception):
    def __init__(self, mensaje="", linea=0):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.linea = linea
```

---

## 7. RECURSIVIDAD

```python
# Factorial recursivo
def factorial(n):
    if n == 1:        # caso base
        return 1
    return n * factorial(n - 1)  # paso recursivo

# Fibonacci recursivo
def fib(n):
    if n == 0 or n == 1:  # caso base
        return n
    return fib(n-1) + fib(n-2)

# Torres de Hanoi (movimientos mínimos = 2^n - 1)
def hanoi_movimientos(n):
    if n == 1:
        return 1
    return 2 * hanoi_movimientos(n-1) + 1
```

**Sin caso base** → `RecursionError` (pila agotada).
**Límite:** `sys.setrecursionlimit(2000000)`.

---

## 8. ZIP & ENUMERATE

```python
# Zip: une listas en pares
list(zip([1,2,3], ["a","b","c"]))  # [(1,'a'), (2,'b'), (3,'c')]

# Crear diccionario desde dos listas
dict(zip(claves, valores))

# Enumerate: índices automáticos
for i, val in enumerate(["a","b","c"]):
    print(i, val)  # 0 a, 1 b, 2 c

# Diccionario por comprensión
registro = {key: value for key, value in zip(fields, values)}
```

---

## 9. UNPACKING (Desempaquetado)

```python
a, b, c = [1, 2, 3]          # mismo número de vars
a, *b, c = [1,2,3,4,5]       # b = [2,3,4]
*a, b = [1,2,3,4]            # a = [1,2,3], b = 4
a, b, *c = [1,2,3,4]         # c = [3,4]

# Diccionarios
k1, k2, k3 = {"a":1, "b":2, "c":3}  # claves
x, y, z = dict.values()             # valores

# Fusionar diccionarios
d3 = {**d1, **d2}
```

---

## 10. ALGORITMOS CLAVE

### Número primo

```python
def es_primo(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
```

### Fibonacci iterativo

```python
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
```

### Max / Min / Media

```python
max(lista)
min(lista)
sum(lista) / len(lista)
```

### Moda (diccionario de frecuencias)

```python
frecuencias = {}
for item in lista:
    frecuencias[item] = frecuencias.get(item, 0) + 1
moda = max(frecuencias, key=frecuencias.get)
```

### Factorización en primos

```python
def factorizar(n):
    factores = []
    for i in range(2, n + 1):
        while n % i == 0:
            factores.append(i)
            n = n // i
    return factores
```

---

## 11. BENCHMARKS (Medir tiempo)

```python
import time
t0 = time.time()
# código a medir
t1 = time.time()
print(t1 - t0)  # segundos

# Con timeit (más preciso)
from timeit import timeit as t
t(lambda: funcion(), number=1000)
```

---

## 12. LIBRERÍAS DEL SISTEMA

```python
import platform
platform.system()      # "Windows", "Linux", etc.
platform.processor()   # nombre del procesador
platform.machine()     # arquitectura

import psutil
psutil.virtual_memory().total  # RAM total en bytes

import os
os.name  # nombre del SO

import sys
sys.getrecursionlimit()
sys.setrecursionlimit(2000000)
```

