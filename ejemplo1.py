def agregar_vertice(graph, vertex):
    '''
    Funcion: Esta función agrega un vértice al grafo si no está presente.

    Parametro: graph vertex

    Retorna: no retorna ningun valor
    '''
    #verifica si el vértice ya existe en el grafo. Si no existe, se crea una nueva entrada en el diccionario del grafo con la clave del nuevo vértice y una lista vacía como valor
    if vertex not in graph:
    #agregar nuevos vértices al grafo de manera dinámica.
        graph[vertex] = []

def agregar_arista(graph, vertex1, vertex2):
    '''
    Funcion:Su objetivo es agregar una arista que conecte los vértices "vertex1" y "vertex2" al grafo.

    Parametro:graph, vertex1, vertex2

    Retorna: no retorna ningun valor
    '''
    #llama a la función "agregar_vertice" para agregar el vértice "vertex1" al grafo. Si el vértice ya existe en el grafo, la función simplemente no hace nada. Si no existe, se agrega el vértice al grafo.
    agregar_vertice(graph, vertex1)
    #La segunda línea hace lo mismo para el vértice "vertex2".
    agregar_vertice(graph, vertex2)
    #La tercera línea agrega el vértice "vertex2" a la lista de vecinos del vértice "vertex1" en el grafo. Esta línea conecta los dos vértices mediante una arista. Si "vertex2" ya se encuentra en la lista de vecinos de "vertex1", la línea simplemente agrega otra conexión entre los mismos vértices, permitiendo grafos con múltiples aristas entre los mismos vértices.
    graph[vertex1].append(vertex2)

def ingresar_grafo():
    '''
    Funcion: La función devuelve el grafo completo después de que el usuario ha terminado de ingresar los vértices y aristas.

    Parametro: no contiene parametros

    Retorna: retorna el grafico 
    '''
    # se inicializa un diccionario vacío llamado "graph" que se utilizará para representar el grafo.
    graph = {}
    #En el bucle "while True", se solicita al usuario que ingrese el vértice 1. Si el usuario ingresa "0", el bucle se detiene y la función devuelve el grafo. 
    while True:
        #Si el usuario ingresa un número diferente de "0", se guarda en la variable "vertex1".
        print("Ingrese el vértice 1 (0 para terminar): ", end="")
        vertex1 = int(input())
        if vertex1 == 0:
            break
        #se solicita al usuario que ingrese el vértice 2 y se guarda en la variable "vertex2".
        print("Ingrese el vértice 2: ", end="")
        vertex2 = int(input())
        agregar_arista(graph, vertex1, vertex2)
    #El bucle continúa ejecutándose hasta que el usuario ingresa "0", momento en el que se devuelve el grafo completo.
    return graph

if __name__ == '__main__':
    #llamamos a la funcion 
    graph = ingresar_grafo()
    # se imprime los datos 
    print(graph)
