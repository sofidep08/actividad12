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

diccionario={}
lista=[]
cantidad= int(input("Ingrese la cantidad de personas que desea registrar: "))
for i in range(cantidad):
    nombre=input("Ingrese el nombre del repartidor: ")
    paquetes=int(input("Ingrese los paquetes entregados: "))
    zona=input("Zona de trabajo: ")
    diccionario[nombre]={
        "paquetes":paquetes,
        "zona":zona
    }
    empleados2=quick_sort(diccionario[paquetes])
    empleados1=nombre,paquetes,zona
    lista.append(empleados1)

