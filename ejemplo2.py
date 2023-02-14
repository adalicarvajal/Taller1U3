class GrafoNoDirigido:
    '''
    La clase "GrafoNoDirigido" proporciona métodos para agregar vértices y aristas al grafo, para obtener los vértices y aristas del grafo,
    y para verificar si un vértice o una arista determinados existen en el grafo. También puede proporcionar métodos para recorrer y buscar en el grafo, dependiendo de la aplicación.
    '''
    def __init__(self):
        '''
        Funcion:La función __init__(self) es el método constructor de la clase GrafoNoDirigido, que se llama automáticamente cuando se crea un nuevo objeto de esta clase.

        Parametros:

        Retorna:
        '''
        # se utiliza en el método constructor de la clase GrafoNoDirigido para inicializar el atributo vertices como un diccionario vacío.
        self.vertices = {}
    
    def agregar_vertice(self, v):
        '''
        Funcion: sirve para agregar un nuevo vértice al grafo representado por la clase GrafoNoDirigido. Si el vértice ya existe en el grafo, la función no hace nada.

        Parametros:

        Retorna:

        '''
        #la función verifica si el vértice v no está ya en el diccionario vertices del objeto de la clase. Si no se encuentra el vértice, entonces la función continúa, de lo contrario, no hace nada.
        if v not in self.vertices:
            #se agrega un nuevo par clave-valor al diccionario vertices del objeto de la clase. La clave es el vértice v, y el valor es un conjunto vacío, que representa los vecinos del vértice v.
            self.vertices[v] = set()
    
    def agregar_arista(self, v1, v2):
        '''
        Funcion:La función agregar_arista(self, v1, v2) es un método de la clase GrafoNoDirigido que se utiliza para agregar una nueva arista (o conexión) entre dos vértices del grafo.

        Parametros:

        Retorna:

        '''
        # la función verifica si los vértices v1 y v2 están en el diccionario vertices del objeto de la clase. Si ambos vértices se encuentran en el grafo, entonces la función continúa, de lo contrario, no hace nada.
        if v1 in self.vertices and v2 in self.vertices:
            #se agrega el vértice v2 al conjunto de vecinos del vértice v1.
            self.vertices[v1].add(v2)
            # se agrega el vértice v1 al conjunto de vecinos del vértice v2.
            self.vertices[v2].add(v1)
    
    def __str__(self):
        '''
        Funcion: La función recorre todos los vértices del grafo y para cada uno de ellos, agrega una línea a la cadena de salida que contiene el vértice y sus vecinos. 
        Cada vecino se separa del siguiente por un espacio en blanco, mientras que cada línea se separa de la siguiente por un carácter de nueva línea.

        Parametros: self 

        Retorna: res

        '''
        #se crea una cadena vacía llamada res para almacenar la representación en cadena del grafo.
        res = ""
        #se comienza un ciclo for que recorre todos los vértices del grafo.
        for v in self.vertices:
            # se agrega el vértice v actual a la cadena res y se le agrega un carácter de dos puntos (:) para separar el vértice de sus vecinos.
            res += str(v) + ": "
            #se comienza otro ciclo for que recorre todos los vecinos del vértice v
            for vecino in self.vertices[v]:
                #se agrega cada vecino a la cadena res y se le agrega un espacio en blanco para separarlo del siguiente vecino.
                res += str(vecino) + " "
            # se agrega un carácter de nueva línea (\n) para separar el vértice actual de los siguientes en la representación del grafo.
            res += "\n"
        # la función devuelve la cadena res que contiene la representación del grafo en forma de cadena.
        return res

# Ejemplo de uso
grafo = GrafoNoDirigido()

# Agregar vértices
v1 = input("Ingrese el vértice 1: ")
grafo.agregar_vertice(v1)

v2 = input("Ingrese el vértice 2: ")
grafo.agregar_vertice(v2)

v3 = input("Ingrese el vértice 3: ")
grafo.agregar_vertice(v3)

# Agregar aristas
a1 = input("Ingrese la arista 1 (en el formato 'v1 v2'): ")
v1, v2 = a1.split()
grafo.agregar_arista(v1, v2)

a2 = input("Ingrese la arista 2 (en el formato 'v1 v2'): ")
v1, v2 = a2.split()
grafo.agregar_arista(v1, v2)

# Imprimir grafo
print(grafo)
