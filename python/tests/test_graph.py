import pytest

from data_structure.graph.graph import  Graph, Vertex

def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44


# Test breadth_first_search
# ------------------------------------------------

def test_breadth_first_search_case1(simple_graph):
    # Arrange
    expected = [1, 5 ,2 ,3, 4]

    # Act
    actual = simple_graph[0].breadth_first_search(simple_graph[1])

    # Assert
    assert actual == expected


def test_breadth_first_search_case2(example_graph):
    # Arrange
    expected = ['Pandora', 'Arandelle', 'Metroville', 'Monstropolis', 'Naboo', 'Narnia']

    # Act
    actual = example_graph[0].breadth_first_search(example_graph[1])

    # Assert
    assert actual == expected

def test_breadth_first_search_single():
    # Arrange
    graph = Graph()
    vertex_1 = graph.add_node(1)

    expected = [1]

    # Act
    actual = graph.breadth_first_search(vertex_1)

    # Assert
    assert actual == expected

def test_breadth_first_search_empty():
    # Arrange
    graph = Graph()

    # Assert
    with pytest.raises(Exception):
        assert graph.breadth_first_search(graph)



# -----------------------------------------------
# TEST DEPTH FIRST


def test_depth_first(depth_first):
    #Arrange
    expected = 'A,B,C,G,D,E,H,F,'

    # actual

    actual = depth_first[0].depth_first(depth_first[1])
    assert actual == expected

def test_depth_first_one_node_graph():
    #Arrange
    expected = 'None,'
    graph = Graph()
    empty=graph.add_node(None)

    # actual

    actual = graph.depth_first(empty)
    assert actual == expected


def test_depth_first_empty(depth_first):
    #Arrange
    graph = Graph()

    # actual
    with pytest.raises(Exception):
        assert graph.depth_first(graph)

# Fixtures
# ------------------------------------------------
@pytest.fixture
def simple_graph():
    graph = Graph()

    vertex_1 = graph.add_node(1)

    vertex_2 = graph.add_node(2)

    vertex_3 = graph.add_node(3)

    vertex_4 = graph.add_node(4)

    vertex_5 = graph.add_node(5)

    graph.add_edge(vertex_1,vertex_5)

    graph.add_edge(vertex_1,vertex_2)

    graph.add_edge(vertex_1,vertex_3)

    graph.add_edge(vertex_5,vertex_3)

    graph.add_edge(vertex_3,vertex_4)

    return graph, vertex_1

@pytest.fixture
def example_graph():
    graph = Graph()

    pandora = graph.add_node('Pandora')
    arandelle = graph.add_node('Arandelle')
    metroville = graph.add_node('Metroville')
    monstropolis = graph.add_node('Monstropolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_edge(pandora, arandelle)
    graph.add_edge(arandelle, pandora)

    graph.add_edge(arandelle, metroville)
    graph.add_edge(metroville, arandelle)

    graph.add_edge(arandelle, monstropolis)
    graph.add_edge(monstropolis, arandelle)

    graph.add_edge(metroville, naboo)
    graph.add_edge(naboo, metroville)

    graph.add_edge(monstropolis, naboo)
    graph.add_edge(naboo, monstropolis)

    graph.add_edge(metroville, narnia)
    graph.add_edge(narnia, metroville)

    graph.add_edge(narnia, naboo)
    graph.add_edge(naboo, narnia)

    return graph, pandora

@pytest.fixture()
def depth_first():

    graph =Graph()
    anode=graph.add_node('A')
    bnode=graph.add_node('B')
    dnode=graph.add_node('D')
    fnode=graph.add_node('F')
    cnode=graph.add_node('C')
    enode=graph.add_node('E')
    hnode=graph.add_node('H')
    gnode=graph.add_node('G')

    graph.add_edge(anode,bnode)
    graph.add_edge(bnode,anode)

    graph.add_edge(bnode,cnode)
    graph.add_edge(cnode,bnode)

    graph.add_edge(bnode,dnode)
    graph.add_edge(dnode,bnode)

    graph.add_edge(cnode,gnode)
    graph.add_edge(gnode,cnode)

    graph.add_edge(anode,dnode)
    graph.add_edge(dnode,anode)

    graph.add_edge(dnode,enode)
    graph.add_edge(enode,dnode)

    graph.add_edge(dnode,hnode)
    graph.add_edge(hnode,dnode)

    graph.add_edge(dnode,fnode)
    graph.add_edge(fnode,dnode)

    graph.add_edge(hnode,fnode)
    graph.add_edge(fnode,hnode)


    return graph, anode


