def graph_coloring(current_vertex):
    global result

    # Base case: All vertices are colored
    if current_vertex > n:
        result = True
        return

    for color in colors:
        is_valid_color = True
        for neighbor in graph[current_vertex]:
            # same color should not be there
            if coloring[neighbor] == color:
                is_valid_color = False
                break

        if is_valid_color:
            coloring[current_vertex] = color
            graph_coloring(current_vertex + 1)
            if result:
                return

            # Backtrack
            coloring[current_vertex] = None

# Define graph, colors, and other variables

n = 6
graph = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5], 5: [2, 4], 6: [3]}
colors = ['Red', 'Blue', 'Green']
coloring = {i: None for i in range(1, n + 1)} # initially no coloring
result = False

# Start with the first vertex
graph_coloring(1)

if result:
    print("Valid graph coloring exists.")
else:
    print("No valid graph coloring exists.")
