class Nodo:
    """
    Clase que representa un nodo en una lista simplemente ligada.
    """
    def __init__(self, data):
        self.data = data
        self.siguiente = None

    def __repr__(self):
        return f"Node({self.data})"