'''Here's an example code to create a graph in Python using Object-Oriented Programming (OOP):'''

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_neighbors(self):
        return self.neighbors

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node

    def add_edge(self, node1, node2):
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def display_graph(self):
        for node in self.nodes:
            print(node.value, "->", [n.value for n in node.neighbors])

# Example usage:
graph = Graph()
node1 = graph.add_node("A")
node2 = graph.add_node("B")
node3 = graph.add_node("C")

graph.add_edge(node1, node2)
graph.add_edge(node2, node3)
graph.add_edge(node1, node3)

graph.display_graph()

'''This code defines two classes: Node and Graph. The Node class represents a node in the graph, with attributes for its value and a list of neighboring nodes. The Graph class represents the graph itself, with methods to add nodes and edges, and a method to display the graph.

In the example usage, we create a graph with three nodes (A, B, and C) and add edges between them. Finally, we display the graph using the display_graph method.

Note: This is a basic implementation, and you may want to add more methods and features depending on your specific use case.'''