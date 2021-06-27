from collections import deque
class Vertex:
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return f"{self.data}"
class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)
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
 
# if __name__ == '__main__':
#     graph = Graph()
#     node_a = graph.add_node('a')
#     node_b = graph.add_node('b')
#     node_c = graph.add_node('c')
#     node_d = graph.add_node('d')
#     node_e = graph.add_node('e')
#     node_f = graph.add_node('f')
#     graph.add_edge(node_a,node_c)
#     graph.add_edge(node_a,node_d)
#     graph.add_edge(node_b,node_c)
#     graph.add_edge(node_b,node_f)
#     graph.add_edge(node_c,node_e)
#     graph.add_edge(node_d ,node_e)
#     graph.add_edge(node_e,node_f)
#     print(graph.get_nodes())
#     print(graph.get_neighbors(node_a))
#     print(graph.get_neighbors(node_b))
#     print(graph.get_neighbors(node_c))
#     print(graph.get_neighbors(node_d))
#     print(graph.get_neighbors(node_e))
#     print(graph.get_neighbors(node_f))
#     print(graph.size())
#     graph.breadth_first_search(node_a, lambda v: print(v.data))