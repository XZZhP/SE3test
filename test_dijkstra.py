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
        expected = {'A': 0, 'B': 4, 'C': 2, 'D': 5}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected)

    def test_single_node(self):
        graph = {'A': {}}
        expected = {'A': 0}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected)

    def test_disconnected_graph(self):
        graph = {
            'A': {'B': 1},
            'B': {'A': 1},
            'C': {'D': 2},
            'D': {'C': 2}
        }
        # 修正期望结果，包含所有节点，不可达节点距离为无穷大
        expected = {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected)

    def test_update_distance(self):
        # 测试通过更短路径更新距离的情况
        graph = {
            'A': {'B': 5, 'C': 2},
            'B': {'C': -3},  # 注意：Dijkstra不适用于负权重，这里仅用于测试逻辑
            'C': {}
        }
        # 正确的最短路径应为 A->B (5), A->C (2), B->C (5-3=2)
        # 但由于Dijkstra算法特性，它会先确定C的距离为2，后续不会更新
        # 所以我们期望的结果是基于贪心选择的
        expected = {'A': 0, 'B': 5, 'C': 2}
        result = dijkstra(graph, 'A')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()