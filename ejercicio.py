"""Desarrolle un programa en cualquier lenguaje de programacion que permita: 

1. Crear un Grafo

2. Visualizar el Grafo

3. Agregar un nodo al grafo

4. Buscar el camino de un nodo A a un nodo B
"""

#Trabajo hecho por Milton Yecid Perea y Cristian Ríos

class Grafo:
    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.num_vertices = 0

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            self.num_vertices += 1
            for fila in self.aristas:
                fila.append(0)
            self.aristas.append([0] * self.num_vertices)

    def agregar_arista(self, vertice_origen, vertice_destino):
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            indice_origen = self.vertices.index(vertice_origen)
            indice_destino = self.vertices.index(vertice_destino)
            self.aristas[indice_origen][indice_destino] = 1
            self.aristas[indice_destino][indice_origen] = 1

    def obtener_vertices(self):
        return self.vertices

    def visualizar_grafo(self):
        return self.aristas
    
    def buscar_camino(self, vertice_origen, vertice_destino):
        visitados = set()
        camino = []
        self._dfs_buscar_camino(vertice_origen, vertice_destino, visitados, camino)
        return camino

    def _dfs_buscar_camino(self, vertice_actual, vertice_destino, visitados, camino):
        visitados.add(vertice_actual)
        camino.append(vertice_actual)

        if vertice_actual == vertice_destino:
            return

        for i in range(self.num_vertices):
            if self.aristas[self.vertices.index(vertice_actual)][i] == 1 and self.vertices[i] not in visitados:
                self._dfs_buscar_camino(self.vertices[i], vertice_destino, visitados, camino)
                if camino[-1] == vertice_destino:
                    return

        camino.pop()



# Crear un grafo de ejemplo
mi_grafo = Grafo()
mi_grafo.agregar_vertice("A")
mi_grafo.agregar_vertice("B")
mi_grafo.agregar_vertice("C")
mi_grafo.agregar_arista("A", "B")
mi_grafo.agregar_arista("A", "C")
mi_grafo.agregar_arista("B", "C")

# Obtener la matriz de adyacencia
matriz_adyacencia = mi_grafo.visualizar_grafo()

#print(matriz_adyacencia)
# Imprimir la matriz de adyacencia
#for fila in matriz_adyacencia:
#    print(fila)

# Añadir un nuevo vértice al grafo
mi_grafo.agregar_vertice("D")
mi_grafo.agregar_arista("C", "D")
mi_grafo.agregar_arista("A", "D")

matriz_adyacencia = mi_grafo.visualizar_grafo()

# Imprimir la matriz de adyacencia
for fila in matriz_adyacencia:
    print(fila)

# Buscar un camino entre "A" y "D"
camino = mi_grafo.buscar_camino("B", "D")

if len(camino) > 0:
    print("Camino encontrado:", "->".join(camino))
else:
    print("No se encontró un camino entre los nodos especificados.")