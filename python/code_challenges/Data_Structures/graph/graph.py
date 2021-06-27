class Vertex:
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return f"{self.data}"
class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
class Graph:
    def __init__(self):
        self.adj_arr = {}
    def add_node(self, data):
        node = Vertex(data)
        self.adj_arr[node] = []
        return node
    def add_edge(self,node1=None,node2=None,weight1=0):
        if node1 not in self.adj_arr:
            raise KeyError
        elif node2 not in self.adj_arr:
            raise KeyError
        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adj_arr[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adj_arr[node2].append(edge)
    def get_nodes(self):
       return self.adj_arr.keys()
    def get_neighbors(self,node):
        return self.adj_arr.get(node,[])
    def size(self):
        return len(self.adj_arr)