"""
Given a list of projects, and a list of dependencies (which is a list of
    pairs of projects, where second project is dependent on first project)
    All of a project's dependencies must be built before the project is.
    Find a build order that will allow the projects to be built. If there
    is no valid build order, return an error.

Strategy:
    - Place dependencies on a DAG, recursively find root of graph, and
    delete, thus finding the build order.
"""
from collections import defaultdict


PROJECTS = ['a', 'b', 'c', 'd', 'e', 'f']

DEPENDENCIES = [
    ('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('e', 'e')
]


class Graph:
    """Represent graph using adjacency list"""

    def __init__(self):
        self._graph = defaultdict(list)

    def __iter__(self):
        return iter(dict((k, v) for k, v in self._graph.items()))

    def __getitem__(self, item):
        return self._graph[item]

    def __setitem__(self, u, v):
        self._graph[u].append(v)

    def __delitem__(self, key):
        del self._graph[key]

    def __repr__(self):
        return str(self._graph)

    @property
    def children(self):
        children = []
        for v in self._graph.values():
            children.extend(v)

        return children

    @property
    def parents(self):
        return self._graph.keys()

    @property
    def root(self):
        return (
            set(self.children).symmetric_difference(set(self.parents))
        ).intersection(set(self.children))

    @property
    def leaf(self):
        return (
            set(self.children).symmetric_difference(set(self.parents))
        ).intersection(set(self.parents))


BUILD_ORDER = []


def build_order(graph):

    if graph.root:
        for root in list(graph.root):
            BUILD_ORDER.append(root)
            for k in graph:
                if root in graph[k]:
                    del graph[k]
        build_order(graph)
    else:
        # add independent nodes to build order
        for k in graph:
            BUILD_ORDER.append(k)


def main():

    # build graph
    g = Graph()
    for d in DEPENDENCIES:
        g[d[0]] = d[1]
    # find leaves
    leaves = list(g.leaf)

    # find build order
    build_order(g)
    # add leaves to final build order

    BUILD_ORDER.extend(leaves)

    print(BUILD_ORDER)

if __name__ == "__main__":
    main()
