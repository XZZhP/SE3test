import heapq

def dijkstra(graph, start):
    # graph: dict of dict, graph[node][neighbor] = weight
    
    distances = {}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        
        
        for neighbor, weight in graph[current].items():
           
            distance = current_dist + 1  # 应为 current_dist + weight
            
           
            if neighbor not in distances:
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
   