from Nodo import Nodo
from ListaLigada import ListaLigada

lista = ListaLigada()

print("¿La lista está vacía?", lista.esta_vacio())  # Output: True

lista.agregar_final_lista(10)
lista.agregar_final_lista(20)
lista.agregar_final_lista(30)

print("Lista después de agregar al final:", lista) 

# Agregar un nodo al inicio de la lista
lista.agregar_inicio_lista(5)
print("Lista después de agregar al inicio:", lista)  

# Agregar un nodo usando el alias agregar_dato (equivale a agregar_final_lista)
lista.agregar_dato(40)
print("Lista después de agregar dato (alias):", lista) 

# Insertar un nodo después de un nodo existente
exito = lista.insertar_luego_de(20, 25)
print("Inserción exitosa:", exito)  # Output: True
print("Lista después de insertar luego de 20:", lista) 

# Intentar insertar después de un nodo que no existe
exito = lista.insertar_luego_de(100, 105)
print("Inserción exitosa:", exito)  # Output: False
print("Lista después de intentar insertar luego de 100:", lista) 

# Buscar un nodo existente
nodo_encontrado = lista.buscar(25)
print("Nodo encontrado:", nodo_encontrado) 

# Buscar un nodo que no existe
nodo_encontrado = lista.buscar(100)
print("Nodo encontrado:", nodo_encontrado)

# Eliminar un nodo existente
exito = lista.eliminar(20)
print("Eliminación exitosa:", exito)
print("Lista después de eliminar 20:", lista)  

# Eliminar la cabeza de la lista
exito = lista.eliminar(5)
print("Eliminación exitosa:", exito)  
print("Lista después de eliminar 5:", lista)

# Intentar eliminar un nodo que no existe
exito = lista.eliminar(100)
print("Eliminación exitosa:", exito)  
print("Lista después de intentar eliminar 100:", lista)  

# Verificar el tamaño de la lista
print("Tamaño de la lista:", len(lista)) 

# Iterar sobre la lista
print("Elementos de la lista:")
for dato in lista:
    print(dato)

