class ListaLigada:
    """
    Clase que representa una lista simplemente ligada.
    """
    def __init__(self):
        self.nodo_cabeza = None
        self.longitud = 0

    def esta_vacio(self):
        """
        Verifica si la lista está vacía.
        """
        return self.nodo_cabeza is None

    def agregar_nodo(self, nodo_actual, nuevo_nodo):
        """
        Agrega un nuevo nodo a la lista ligada.
        """
        nodo_actual.siguiente = nuevo_nodo
        print(f"Append: Añadido {nuevo_nodo} al final de la lista.")

    def agregar_final_lista(self, data):
        """
        Añade un nuevo nodo con el dato especificado al final de la lista.
        """
        nuevo_nodo = Nodo(data)

        if self.esta_vacio():
            self.nodo_cabeza = nuevo_nodo
            print(f"Append: Añadido {nuevo_nodo} como cabeza de la lista.")
        else:
            nodo_actual = self.nodo_cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            self.agregar_nodo(nodo_actual=nodo_actual, nuevo_nodo=nuevo_nodo)
        self.longitud += 1

    def agregar_dato(self, data):
        """
        Alias para el método agregar_final_lista.
        """
        self.agregar_final_lista(data)

    def agregar_inicio_lista(self, data):
        """
        Añade un nuevo nodo con el dato especificado al inicio de la lista.
        """
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.nodo_cabeza
        self.nodo_cabeza = nuevo_nodo
        self.longitud += 1  # Corregido de self.size a self.longitud
        print(f"Prepend: Añadido {nuevo_nodo} al inicio de la lista.")

    def insertar_luego_de(self, objetivo, data):
        """
        Inserta un nuevo nodo con el dato especificado después del nodo que contiene el dato objetivo.
        Retorna True si la inserción fue exitosa, False si el objetivo no se encontró.
        """
        nodo_actual = self.nodo_cabeza
        while nodo_actual:
            if nodo_actual.data == objetivo:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                self.longitud += 1
                print(f"Insert_after: Añadido {nuevo_nodo} después de {nodo_actual}.")
                return True
            nodo_actual = nodo_actual.siguiente
        print(f"insertar_luego: No se encontró el nodo con dato {objetivo}.")
        return False

    def eliminar(self, data):
        """
        Elimina el primer nodo que contiene el dato especificado.
        Retorna True si el nodo fue eliminado, False si no se encontró.
        """
        nodo_actual = self.nodo_cabeza
        nodo_anterior = None
        while nodo_actual:
            if nodo_actual.data == data:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    print(f"Delete: Eliminado {nodo_actual} de la lista.")
                else:
                    self.nodo_cabeza = nodo_actual.siguiente
                    print(f"Delete: Eliminado {nodo_actual}, ahora la cabeza es {self.nodo_cabeza}.")
                self.longitud -= 1
                return True
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        print(f"eliminar: No se encontró el nodo con dato {data}.")
        return False

    def buscar(self, data):
        """
        Busca y retorna el primer nodo que contiene el dato especificado.
        Retorna None si no se encuentra.
        """
        nodo_actual = self.nodo_cabeza
        while nodo_actual:
            if nodo_actual.data == data:
                print(f"Find: Encontrado {nodo_actual}.")
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        print(f"buscar: No se encontró el nodo con dato {data}.")
        return None

    def __len__(self):
        """
        Retorna el número de nodos en la lista.
        """
        return self.longitud

    def __iter__(self):
        """
        Permite iterar sobre los datos de la lista.
        """
        nodo_actual = self.nodo_cabeza
        while nodo_actual:
            yield nodo_actual.data
            nodo_actual = nodo_actual.siguiente

    def __repr__(self):
        """
        Retorna una representación en cadena de la lista.
        """
        datos = " -> ".join(str(data) for data in self)
        return f"ListaLigada({datos})"

