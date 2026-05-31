import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue to hold (distance, node) tuples
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Skip if we've already found a shorter path to this node
        if current_dist > distances[current]:
            continue
            
        # Check neighbors of current node
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            # If we found a shorter path to the neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances