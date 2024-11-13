def a_star(graph, start, goal, heuristic):
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
                    heuristic_cost = cost + distance + heuristic[neighbor]
                    heapq.heappush(queue, (heuristic_cost, neighbor, path + [neighbor]))

heuristic = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print("A*:", a_star(graph, 'A', 'D', heuristic))


# def a_star(graph, start, goal, heuristic):
#     queue = [(0 + heuristic[start], 0, start, [start])]
#     visited = set()
    
#     while queue:
#         _, cost, node, path = heapq.heappop(queue)
        
#         if node in visited:
#             continue
        
#         visited.add(node)
        
#         if node == goal:
#             return cost, path
        
#         for neighbor, weight in graph[node]:
#             if neighbor not in visited:
#                 new_cost = cost + weight
#                 heapq.heappush(queue, (new_cost + heuristic[neighbor], new_cost, neighbor, path + [neighbor]))
    
#     return float("inf"), []

# print(a_star(graph, 'A', 'D', heuristic))
