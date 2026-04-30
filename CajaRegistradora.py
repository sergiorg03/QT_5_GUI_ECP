# Caja registradora con billetes de vuelta infinitos

def calcular_cambio_monedas(importe_productos, cantidad_cliente):
    # Calcular el cambio a devolver
    cambio = round(cantidad_cliente - importe_productos, 2)

    MONEDAS = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cambio_a_devolver = {}

    # Comprobar si se le devuelve
    if cambio < 0: # Debe pagar más
        raise ValueError("ERROR: El cliente no ha dado suficiente dinero. ")
    elif cambio == 0: # Ha pagado el importe justo
        return cambio_a_devolver
    else: # Devolver cambio
        print(f"El cambio a devolver es: {cambio}")
        for moneda in MONEDAS:
            if cambio >= moneda: # Comprobamos que el cambio es mayor que la moneda elegida
                cantidad_monedas = int(cambio // moneda) # Obtenemos el número de monedas que podemos devolver
                cambio_a_devolver[moneda] = cantidad_monedas # añadimos la moneda al diccionario
                cambio = round(cambio - cantidad_monedas * moneda, 2) # actualizamos el cambio
        return cambio_a_devolver

while True:
    importe_productos = float(input("Introduzca el importe de los productos: "))
    cantidad_cliente = float(input("Introduzca la cantidad entregada por el cliente: "))
    try:
        cambio = calcular_cambio_monedas(importe_productos, cantidad_cliente)
        print(f"El cambio a devolver es: {cambio}")
    except ValueError as e:
        print(f"{e}")