import heapq

def dijkstra(graph, start):
    # graph: dict of dict, graph[node][neighbor] = weight
    
    distances = {}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Skip if we've already found a shorter path to this node
        if current_dist > distances.get(current, float('inf')):
            continue
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            # Only consider this new path if it's better
            if neighbor not in distances or distance < distances[neighbor]:
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
   