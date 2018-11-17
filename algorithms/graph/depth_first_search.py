"""
Depth First Search
- exhaustively search a given branch before going onto
a neighbour
- Must check that a given node has been visited, or we get
could get stuck in an inf. loop
"""
from collections import defaultdict


class Graph:
    """Represent graph using adjacency list"""

    def __init__(self):
        self._graph = defaultdict(list)

    def __iter__(self):
        return iter((k, v) for k, v in self._graph.items())

    def __getitem__(self, item):
        return self._graph[item]

    def __setitem__(self, u, v):
        self._graph[u].append(v)

    def __repr__(self):
        return str(self._graph)


class DFS:
    """Operates on Graph objects"""

    def __init__(self, graph):
        self._graph = graph
        self._visited = {k: False for k, v in graph}

    def visit(self, v):
        """Mark visited Nodes"""
        self._visited[v] = True

    def search(self, root):

        #  mark root node as visited
        self.visit(root)
        print(root)

        for node in self._graph[root]:
            if not self._visited[node]:
                self.search(node)


def main():
    """
	Test out DFS implementation on graph:

	0 -> 1 -> 2 ->3
	^
	|
	2
	"""
    g = Graph()
    g[0] = 1
    g[0] = 2
    g[1] = 2
    g[2] = 0
    g[2] = 3
    g[3] = 3

    print(g)

    DFS(g).search(0)


if __name__ == "__main__":
    main()
