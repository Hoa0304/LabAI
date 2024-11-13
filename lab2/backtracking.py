def is_valid(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors.get(neighbor) == color:
            return False
    return True

def backtrack(graph, colors, node, available_colors):
    if node == len(graph):
        return colors
    for color in available_colors:
        if is_valid(graph, colors, node, color):
            colors[node] = color
            result = backtrack(graph, colors, node + 1, available_colors)
            if result:
                return result
            colors.pop(node)
    return None

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}
colors = {}
available_colors = ['Red', 'Green', 'Blue']
solution = backtrack(graph, colors, 0, available_colors)
print("Map coloring solution:", solution)


def map_coloring(graph, colors):
    color_map = {}

    def can_color(node, color):
        for neighbor in graph[node]:
            if color_map.get(neighbor) == color:
                return False
        return True

    def assign_colors(node):
        if node is None:
            return True
        
        for color in colors:
            if can_color(node, color):
                color_map[node] = color
                if assign_colors(next_node()):
                    return True
                color_map.pop(node)
        return False

    def next_node():
        return next((node for node in graph if node not in color_map), None)

    assign_colors(next_node())
    return color_map

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
print(map_coloring(graph, colors))
