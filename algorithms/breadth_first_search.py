"""
- Main tripping point is assumption that BFS uses recursion
- Actually implemented using a Queue, using an iterative approach

"""

from collections import defaultdict
from queue import Queue

class Graph:
	"""Represent graph using adjacency list"""

	def __init__(self):
		self._graph = defaultdict(list)

	def __iter__(self):
		return iter((k,v) for k, v in self._graph.items())

	def __getitem__(self, item):
		return self._graph[item]

	def __setitem__(self, u, v):
		self._graph[u].append(v)

	def __repr__(self):
		return str(self._graph)


class BFS:
	"""Operates on Graph objects"""

	def __init__(self, graph):
		self._graph = graph
		self._visited = {k: False for k, v in graph}
		self._queue = Queue()


	def visit(self, v):
		"""Mark visited Nodes"""
		self._visited[v] = True


	def search(self, root):

		self.visit(root)
		self._queue.put(root)
		print(root)

		while self._queue:
			
			node_to_examine = self._queue.get()

			for node in self._graph[node_to_examine]:
				if not self._visited[node]:
					print(node)

					self.visit(node)
					self._queue.put(node)

		print("here", self._queue.qsize())

def main():
	"""
	Test out DFS implementation on graph:

	0 -> 1 -> 2 ->3
	^
	|
	2
	"""
	g = Graph()
	g[0]=1 
	g[0]=2
	g[1]=2 
	g[2]=0 
	g[2]=3 
	g[3]=3

	print(g) 

	BFS(g).search(0)

if __name__ == "__main__":
	main()	

