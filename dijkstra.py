import heapq

def dijkstra(graph, start):
    # graph: dict of dict, graph[node][neighbor] = weight
    
    # 初始化所有节点距离为无穷大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # 如果当前节点已经处理过且距离更短，则跳过
        if current_dist > distances.get(current, float('inf')):
            continue
        
        # 检查当前节点是否在图中存在（避免KeyError）
        if current not in graph:
            continue
            
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            # 只有找到更短路径时才更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# 测试用例
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 5, 'D': 10},
        'C': {'A': 2, 'B': 5, 'D': 3},
        'D': {'B': 10, 'C': 3}
    }
    print(dijkstra(graph, 'A'))