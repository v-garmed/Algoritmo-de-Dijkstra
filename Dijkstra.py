import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}        #La distancia a los nodos es "infinita" al inicio.
    distancias[inicio] = 0                                      #El dato inicial es que el origen tiene distancia 0.
    
    Nodo_prioritario= [(0, inicio)]
    visitados = set()

    while Nodo_prioritario:

        distancia_actual, nodo_actual = heapq.heappop(Nodo_prioritario)  #Pasa los datos a Nodo_prioritario, pasando a ser el "nuveo nodo"


        if nodo_actual in visitados:                     #Compara la distancia actual con la distancia guardada 
            continue
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():                   #Recorre los vecinos del nodo actual usando el metodo items()
            if vecino in visitados:
                continue
            distancia = distancia_actual + peso                            #Calcula la distancia al vecino
            
            if distancia < distancias[vecino]:                     #Si la distancia al vecino es menor que la guardada
                distancias[vecino] = distancia                            #Actualiza la distancia al vecino
                heapq.heappush(Nodo_prioritario, (distancia, vecino))

    return distancias

def dibujar_grafo(grafo, distancias):
    G = nx.Graph()

    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_color='black')
    
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    plt.title("Grafo con Dijkstra")
    plt.show()


grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},                      #Grafo generado para el ejemplo 🤖 
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'

distancias = dijkstra(grafo, inicio)
print(f"Distancias desde el nodo {inicio}: {distancias}")
dibujar_grafo(grafo, distancias)  #Dibuja el grafo con las distancias calculadas


