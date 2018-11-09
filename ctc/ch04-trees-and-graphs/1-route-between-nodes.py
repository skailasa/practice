"""
Given a directed graph, design an algorithm to find out
whether a route between two nodes exists.

Can use BFS or DFS to search for a route between nodes.
"""

from collections import defaultdict
from collections import Counter
from queue import Queue


class Graph:
    """
    Represent a graph using an adjacency list
    """

    def __init__(self):
        self._graph = defaultdict(list)

    def __iter__(self):
        return iter((k, v) for k, v in self._graph.items())

    def __getitem__(self, item):
        return self._graph[item]

    def __setitem__(self, key, value):
        self._graph[key].append(value)

    def __repr__(self):
        return str(self._graph)


class Search:
    """
    Base Search class
    """

    def __init__(self, graph):
        self._graph = graph
        self._visited = {k: False for k, v in graph}

    def visit(self, node):
        """Mark visited nodes"""
        self._visited[node] = True

    def search(self, root, searched):
        """search from a given root for 'searched' node"""
        raise NotImplementedError


class DepthFirst(Search):
    """
    Easiest to implement. Search through each branch before
        moving onto next branch.
    """

    def __init__(self, graph):
        super().__init__(graph)
        self._found = False

    def search(self, root, searched):

        check = Counter()
        while not self._found:

            self.visit(root)
            check[root] += 1

            if root == searched:
                print("Connected")
                self._found = True

            for adjacent_node in self._graph[root]:
                if not self._visited[adjacent_node]:
                    self.search(adjacent_node, searched)

            if check[root] > 1:
                print("Not Connected")
                self._found = True


class BreadthFirst(Search):
    """
    Can be implemented using a queue
    """
    def __init__(self, graph):
        super().__init__(graph)
        self._queue = Queue()
        self._connected = None

    def search(self, root, searched):

        self.visit(root)
        self._queue.put(root)

        while self._queue:

            node_to_examine = self._queue.get()

            if node_to_examine == searched:
                self._connected = 'connected'
                break

            for adjacent_node in self._graph[node_to_examine]:
                if not self._visited[adjacent_node]:
                    self.visit(adjacent_node)
                    self._queue.put(adjacent_node)

            if self._queue.empty():
                self._connected = 'not connected'
                break

        print(self._connected)


if __name__ == "__main__":
    g = Graph()

    """g[0] = 1
    g[0] = 2
    g[1] = 2
    g[2] = 0
    g[2] = 3
    g[3] = 3
    g[4] = 4
    g[0] = 10
    g[10] = 10"""

    g[0] = 0
    g[1] = 1

    #DepthFirst(g).search(0, 1)
    BreadthFirst(g).search(0, 0)

    #DFS()
