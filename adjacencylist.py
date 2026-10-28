class GraphList:
    def __init__(self, size):
        self.size = size
        self.adj_list = [[] for _ in range(size)]
        self.vertex_data = [''] * size

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def print_graph(self):
        print("Adjacency List:")
        for vertex in range(self.size):
            neighbors = [self.vertex_data[i] for i in self.adj_list[vertex]]
            print(f"Vertex {self.vertex_data[vertex]} ({vertex}): {neighbors}")

g_list = GraphList(4)
g_list.add_vertex_data(0, 'A')
g_list.add_vertex_data(1, 'B')
g_list.add_vertex_data(2, 'C')
g_list.add_vertex_data(3, 'D')

g_list.add_edge(0, 1)
g_list.add_edge(0, 2)
g_list.add_edge(1, 3)

g_list.print_graph()
