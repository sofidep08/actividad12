
def quick_sort(lista):
    if len(lista) <=1:
        return lista
    pivote = lista[0]
    primero = [x for x in lista[1:] if x < pivote]
    igual = [x for x in lista if x == pivote]
    ultimo = [x for x in lista[1:] if x > pivote]
    return quick_sort(primero) + igual + quick_sort(ultimo)

def buscar_repartidor(diccionario, nombre_buscado):
    for nombre, datos in diccionario.items():
        if nombre.lower() == nombre_buscado.lower():
            return nombre, datos
    return None

def mostrar(diccionario_ordenado):
    print("\nRepartidores registrados")
    for nombre, datos in diccionario_ordenado:
        print(f"Nombre: {nombre}, Paquetes: {datos['paquetes']}, Zona: {datos['zona']}")

diccionario={}
cantidad= int(input("Ingrese la cantidad de personas que desea registrar: "))
for i in range(cantidad):
    nombre=input("Ingrese el nombre del repartidor: ")
    paquetes=int(input("Ingrese los paquetes entregados: "))
    zona=input("Zona de trabajo: ")
    diccionario[nombre]={
        "paquetes":paquetes,
        "zona":zona
    }
lista_ordenada = quick_sort(list(diccionario.items()))

mostrar(lista_ordenada)