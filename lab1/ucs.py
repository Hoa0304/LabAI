import heapq

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, city, path = heapq.heappop(queue)
        if city == goal:
            return cost, path
        if city not in visited:
            visited.add(city)
            for neighbor, distance in graph[city].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + distance, neighbor, path + [neighbor]))
                    
# def ucs(graph, start, goal):
#     queue = [(0, start, [start])]
#     visited = set()
    
#     while queue:
#         cost, node, path = heapq.heappop(queue)
        
#         if node in visited:
#             continue
        
#         visited.add(node)
        
#         if node == goal:
#             return cost, path
        
#         for neighbor, weight in graph[node]:
#             if neighbor not in visited:
#                 heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    
#     return float("inf"), []                    

graph = {
    'A': {'B': 2, 'C': 9, 'D': 10},
    'B': {'A': 2, 'C': 6, 'D': 4},
    'C': {'A': 9, 'B': 6, 'D': 8},
    'D': {'A': 10, 'B': 4, 'C': 8}
}
print("UCS:", ucs(graph, 'A', 'D'))
