"""
Finding Adjacent Nodes

There are two types of graphs; directed and undirected. In an undirected graph, the edges between nodes have no particular direction (like a two-way street) whereas in a directed graph, each edge has a direction associated with it (like a one-way street).

For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.

We can encode graphs using an adjacency matrix. An adjacency matrix for a graph with "n" nodes is an "n * n" matrix where the entry at row "i" and column "j" is a 0 if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are adjacent.

For the example above, the adjacency matrix would be as follows:

[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

A one indicates that a connection is true and a zero indicates a connection is false.

Your task is to determine if two nodes are adjacent in an undirected graph when given the adjacency matrix and the two nodes.

Adjacency Matrix:

[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
Nodes 0,1 should return True.
Nodes 0,2 should return False.

[
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]
Nodes 0,3 should return True.
Nodes 1,4 should return False.

Notes

Graphs may have between 0 and 25,000 nodes.
Time Limit: 100 milliseconds.

"""


def is_adjacent(matrix: list, node1: int, node2: int) -> bool:
    if matrix[node1][node2] == 1:
        return True
    return False


matrix = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]

print(is_adjacent(matrix, 0, 3))  # True
print(is_adjacent(matrix, 1, 4))  # False
