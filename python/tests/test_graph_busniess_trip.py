from data_structure.graph.graph import Graph
from code_challenges.graphbusinesstrip.graph_business_trip import business_trip
import pytest

# Test business_trip
# ------------------------------------------------
def test_business_trip(travel_graph):
    # Arrange
    expected = '$82'

    # Act
    actual = business_trip(travel_graph[0], travel_graph[1])

    # Assert
    assert actual == expected


def test_business_trip_case2(travel_graph):
    # Arrange
    expected = '$115'

    # Act
    actual = business_trip(travel_graph[0], travel_graph[2])

    # Assert
    assert actual == expected

def test_business_trip_none(travel_graph):
    # Arrange
    expected = None

    # Act
    actual = business_trip(travel_graph[0], travel_graph[3])

    # Assert
    assert actual == expected


def test_business_trip_none2(travel_graph):
    # Arrange
    expected = None

    # Act
    actual = business_trip(travel_graph[0], travel_graph[4])

    # Assert
    assert actual == expected

def test_business_trip_none_transit(travel_graph):
    # Arrange
    expected = None

    # Act
    actual = business_trip(travel_graph[0], travel_graph[5])

    # Assert
    assert actual == expected

def test_business_trip_error():
    # Arrange
    graph = Graph()

    # Assert
    with pytest.raises(Exception):
        graph.business_trip(graph, [])



@pytest.fixture
def travel_graph():
    graph = Graph()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstropolis = graph.add_node('Monstropolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, pandora, 150)

    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, pandora, 82)

    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, arendelle, 99)

    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(monstropolis, arendelle, 42)

    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(monstropolis, metroville, 105)

    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, metroville, 26)

    graph.add_edge(monstropolis, naboo, 73)
    graph.add_edge(naboo, monstropolis, 73)

    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(narnia, metroville, 37)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(naboo, narnia, 250)

    list1 = [metroville, pandora]
    list2 = [arendelle, monstropolis, naboo]
    list3 = [naboo, pandora]
    list4 = [narnia, arendelle, naboo]
    list5 = [narnia, naboo, pandora]

    return graph, list1, list2, list3, list4, list5
