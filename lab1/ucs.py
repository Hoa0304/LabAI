import heapq

def ucs(graph, start, goal):
    queue = [(0, start, [start])]  # (cost, current node, path)
    visited = set()
    while queue:
        cost, city, path = heapq.heappop(queue)  # Lấy ra phần tử có chi phí thấp nhất
        if city == goal:  # Nếu tìm thấy đích, trả về chi phí và đường đi
            return cost, path
        if city not in visited:  # Nếu chưa duyệt qua đỉnh này
            visited.add(city)
            for neighbor, distance in graph[city].items():
                if neighbor not in visited:  # Nếu chưa duyệt qua đỉnh kề
                    heapq.heappush(queue, (cost + distance, neighbor, path + [neighbor]))
graph = {
    'A': {'B': 2, 'C': 9, 'D': 10},
    'B': {'A': 2, 'C': 6, 'D': 4},
    'C': {'A': 9, 'B': 6, 'D': 8},
    'D': {'A': 10, 'B': 4, 'C': 8}
}
print("UCS:", ucs(graph, 'A', 'D'))
#================================================================
             

def ucs(graph, start, goal):
    queue = [(0, start, [start])]  # (cost, current node, path)
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)  # Lấy ra phần tử có chi phí thấp nhất
        
        if node in visited:  # Nếu đỉnh đã được duyệt qua, bỏ qua
            continue
        
        visited.add(node)
        
        if node == goal:  # Nếu tìm thấy đích, trả về chi phí và đường đi
            return cost, path
        
        for neighbor, weight in graph[node].items():  # Duyệt các đỉnh kề
            if neighbor not in visited:  # Nếu đỉnh kề chưa duyệt
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    
    return float("inf"), []  # Nếu không tìm thấy đường đi, trả về vô hạn

graph = {
    'A': {'B': 2, 'C': 9, 'D': 10},
    'B': {'A': 2, 'C': 6, 'D': 4},
    'C': {'A': 9, 'B': 6, 'D': 8},
    'D': {'A': 10, 'B': 4, 'C': 8}
}

print("UCS:", ucs(graph, 'A', 'D'))


##================================================================

def uniform_cost_search(graph, start, goal):
    # Khởi tạo hàng đợi ưu tiên với chi phí ban đầu là 0
    frontier = []
    heapq.heappush(frontier, (0, start))  # (chi phí, đỉnh hiện tại)
    
    # Khởi tạo dictionary lưu trữ chi phí tối thiểu đến mỗi đỉnh
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        
        # Nếu đã đến đích, dừng lại và trả về chi phí
        if current_node == goal:
            break
        
        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            
            # Nếu tìm thấy đường đi có chi phí thấp hơn đến đỉnh kề
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node
    
    # Trả về chi phí tối thiểu đến đích
    if goal in cost_so_far:
        return cost_so_far[goal]
    else:
        return None

# Ví dụ đồ thị dưới dạng từ điển (graph)
# Đỉnh là các thành phố, cạnh là đường đi giữa các thành phố với chi phí đi lại
graph = {
    'A': {'B': 2, 'C': 9, 'D': 10},
    'B': {'A': 2, 'C': 6, 'D': 4},
    'C': {'A': 9, 'B': 6, 'D': 8},
    'D': {'A': 10, 'B': 4, 'C': 8}
}

# Chạy thuật toán UCS từ A đến D
start = 'A'
goal = 'D'
result = uniform_cost_search(graph, start, goal)

print(f"Chi phí đi từ {start} đến {goal}: {result}")
