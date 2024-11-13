def greedy(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        _, city, path = heapq.heappop(queue)
        if city == goal:
            return path
        if city not in visited:
            visited.add(city)
            sorted_neighbors = sorted(graph[city].items(), key=lambda x: x[1])
            for neighbor, _ in sorted_neighbors:
                if neighbor not in visited:
                    queue.append((0, neighbor, path + [neighbor]))
                    break

print("Greedy:", greedy(graph, 'A', 'D'))

def greedy_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], start, [start])]
    visited = set()
    
    while queue:
        _, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            return path
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))
    
    return []

heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
print(greedy_search(graph, 'A', 'D', heuristic))
