from code_challenges.Data_Structures.graph.graph import *
import pytest

def test_add_node():
    graph = Graph()
    expected = 'omar'
    actual = graph.add_node('omar').data
    assert actual == expected
def test_add_edge_exists():
    graph = Graph()
    first_node = graph.add_node('omar')
    second_node = graph.add_node('mohammad')
    graph.add_edge(first_node,second_node)
    expected = ['mohammad',0]
    edge = graph.adj_arr[first_node][0]
    actual = [edge.vertex.data,edge.weight]
    assert actual == expected

def test_not_exists():
    with pytest.raises(KeyError):
        graph = Graph()
        first_node = graph.add_node('omar')
        second_node = Vertex('mohammad')
        graph.add_edge(first_node,second_node)
def test_get(graph):
    expected = ['omar', 'mohammad', 'kareem', 'zoubi', 'software', 'engneer']
    nodes = graph.get_nodes()
    actual = []
    for node in nodes:
        actual.append(node.data)
    assert actual == expected
def test_neighbors(graph):
    expected = ['kareem', ['omar', 0], ['mohammad', 0], ['software', 0]]
    nodes = graph.get_nodes()
    for node in nodes:
        if node.data == 'kareem':
            theired_node = node
    neighbors = graph.get_neighbors(theired_node)
    actual = [theired_node.data]
    for edge in neighbors:
        actual += [[edge.vertex.data,edge.weight]]
    assert actual == expected
def test_neighbors_and_wieght(graph_weight):
    expected = ['kareem', ['omar', 1], ['mohammad', 5], ['software', 9]]
    nodes = graph_weight.get_nodes()
    for node in nodes:
        if node.data == 'kareem':
            theired_node = node
    neighbors = graph_weight.get_neighbors(theired_node)
    actual = [theired_node.data]
    for edge in neighbors:
        actual += [[edge.vertex.data,edge.weight]]
    assert actual == expected
def test_get_size(graph):
    expected = 6
    actual = graph.size()
    assert actual == expected
def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert not actual
@pytest.fixture
def graph():
    graph = Graph()
    first_node = graph.add_node('omar')
    second_node = graph.add_node('mohammad')
    theired_node = graph.add_node('kareem')
    fourth_node = graph.add_node('zoubi')
    fifth_node = graph.add_node('software')
    sixth_node = graph.add_node('engneer')
    graph.add_edge(first_node,theired_node)
    graph.add_edge(first_node,fourth_node)
    graph.add_edge(second_node,theired_node)
    graph.add_edge(second_node,sixth_node)
    graph.add_edge(theired_node,fifth_node)
    graph.add_edge(fourth_node ,fifth_node)
    graph.add_edge(fifth_node,sixth_node)
    return graph
@pytest.fixture
def graph_weight():
    graph = Graph()
    first_node = graph.add_node('omar')
    second_node = graph.add_node('mohammad')
    theired_node = graph.add_node('kareem')
    fourth_node = graph.add_node('zoubi')
    fifth_node = graph.add_node('software')
    sixth_node = graph.add_node('engneer')
    graph.add_edge(first_node,theired_node,1)
    graph.add_edge(first_node,fourth_node,3)
    graph.add_edge(second_node,theired_node,5)
    graph.add_edge(second_node,sixth_node,7)
    graph.add_edge(theired_node,fifth_node,9)
    graph.add_edge(fourth_node ,fifth_node,8)
    graph.add_edge(fifth_node,sixth_node,4)
    return graph