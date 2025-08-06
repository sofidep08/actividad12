diccionario={}
lista=[]
def quick_sort(lista):
    if len(lista) <=1:
        return lista
    pivote = lista[0]
    primero = [x for x in lista[1:] if x < pivote]
    igual = [x for x in lista if x == pivote]
    ultimo = [x for x in lista[1:] if x > pivote]
    return quick_sort(primero) + igual + quick_sort(ultimo)

def busqueda(lista,buscando):
    for elementos in lista:
       if elementos == buscando:
            return elementos
       else:
           return print("No esta el empleado")

def mostrar(lista):
    for elementos in lista:
        print(elementos)


cantidad= int(input("Ingrese la cantidad de personas que desea registrar: "))
for i in range(cantidad):
    nombre=input("Ingrese el nombre del repartidor: ")
    paquetes=int(input("Ingrese los paquetes entregados: "))
    zona=input("Zona de trabajo: ")
    diccionario[nombre]={
        "paquetes":paquetes,
        "zona":zona
    }
    lista.append((nombre,paquetes,zona))
    quick_sort(paquetes)
mostrar(lista)

buscar=input("Ingrese al repartidor que desea buscar: ")
encontrado=busqueda(lista,buscar)
print(encontrado)
