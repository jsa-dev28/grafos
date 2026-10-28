from adjacencylist import GraphList
from adjacencymatrix import GraphMatrix
def convert_list_to_matrix(graph_list):
    size = graph_list.size
    new_matrix_graph = GraphMatrix(size)
    new_matrix_graph.vertex_data = list(graph_list.vertex_data)
    
    for u in range(size):
        for v in graph_list.adj_list[u]:
            new_matrix_graph.add_edge(u, v)
            
    return new_matrix_graph

g_list = GraphList(4)
g_list.add_vertex_data(0, 'A')
g_list.add_vertex_data(1, 'B')
g_list.add_vertex_data(2, 'C')
g_list.add_vertex_data(3, 'D')

g_list.add_edge(0, 1)
g_list.add_edge(0, 2)
g_list.add_edge(1, 3)

print("\nGrafo Original: ")
g_list.print_graph()

g_mat_convertido = convert_list_to_matrix(g_list)

print("\nGrafo Convertido: ")
g_mat_convertido.print_graph()
