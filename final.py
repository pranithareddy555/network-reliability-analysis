import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import itertools

# Define the functions from the previous code
def generate_triangles(graph):
    return [triangle for triangle in itertools.combinations(graph.nodes(), 3)]

def remove_edges(graph, triangle):
    for edge in itertools.combinations(triangle, 2):
        if graph.has_edge(*edge):
            graph.remove_edge(*edge)

def is_network_operational(graph):
    return all(len(list(nx.neighbors(graph, node))) > 0 for node in graph.nodes())

def calculate_reliability(triangles, p):
    total_states = 2 ** len(triangles)
    operational_states = 0

    for state in itertools.product([True, False], repeat=len(triangles)):
        graph = nx.complete_graph(5)
        active_triangles = sum(state)

        for triangle, active in zip(triangles, state):
            if not active:
                remove_edges(graph, triangle)

        if is_network_operational(graph):
            operational_states += (p ** active_triangles) * ((1 - p) ** (len(triangles) - active_triangles))

    return operational_states #/ total_states

# Main execution
graph = nx.complete_graph(5)
triangles = generate_triangles(graph)

# Prepare values for plotting
p_values = [] 
for i in range(5, 101, 5): 
    p_values.append(i / 100.0)

reliabilities = [calculate_reliability(triangles, p) for p in p_values]
print(p_values)
print(reliabilities)
# Plotting
plt.plot(p_values, reliabilities, color='red')
plt.xlabel('Probability p')
plt.ylabel('Network Reliability')
plt.title('Network Reliability vs Probability p')
plt.grid(True)
plt.show()
