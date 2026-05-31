import unittest
from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_basic_graph(self):
        graph = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 5, 'D': 10},
            'C': {'A': 2, 'B': 5, 'D': 3},
            'D': {'B': 10, 'C': 3}
        }
        expected_distances = {'A': 0, 'B': 4, 'C': 2, 'D': 5}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected_distances)

    def test_single_node(self):
        graph = {'A': {}}
        expected_distances = {'A': 0}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected_distances)

    def test_disconnected_graph(self):
        graph = {
            'A': {'B': 1},
            'B': {'A': 1},
            'C': {'D': 2},
            'D': {'C': 2}
        }
        # Starting from A, C and D should not be reachable
        # The algorithm will include all nodes in the graph with infinity distance for unreachable ones
        expected_distances = {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected_distances)

    def test_linear_graph(self):
        graph = {
            'A': {'B': 1},
            'B': {'C': 2},
            'C': {'D': 3},
            'D': {}
        }
        expected_distances = {'A': 0, 'B': 1, 'C': 3, 'D': 6}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected_distances)

if __name__ == '__main__':
    unittest.main()