import unittest
from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_basic_case(self):
        graph = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 5, 'D': 10},
            'C': {'A': 2, 'B': 5, 'D': 3},
            'D': {'B': 10, 'C': 3}
        }
        result = dijkstra(graph, 'A')
        expected = {'A': 0, 'B': 4, 'C': 2, 'D': 5}
        self.assertEqual(result, expected)
        
    def test_update_distance_case(self):
        # 这个测试用例应该能暴露算法的问题
        # 从A到B权重为5，从A到C权重为2，从C到B权重为2
        # 正确的最短路径应该是A->C->B，总权重为4
        graph = {
            'A': {'B': 5, 'C': 2},
            'B': {'A': 5, 'C': 2},
            'C': {'A': 2, 'B': 2}
        }
        result = dijkstra(graph, 'A')
        # 在正确实现的Dijkstra算法中，B的最短距离应该是4 (A->C->B)
        # 但在有缺陷的实现中，可能会保持为5 (A->B)
        expected = {'A': 0, 'B': 4, 'C': 2}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()