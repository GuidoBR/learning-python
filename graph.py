# http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default.
    >>> connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    >>> g = Graph(connections, directed=True)
    >>> from pprint import pprint
    >>> pprint(g)
    {'A': {'B'},
    'B': {'D', 'C'},
    'C': {'D'},
    'E': {'F'},
    'F': {'C'}}

    >>> g = Graph(connections)  # undirected
    >>> pprint(g)
    {'A': {'B'},
    'B': {'D', 'A', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'B'},
    'E': {'F'},
    'F': {'E', 'C'}}

    >>> g.add('E', 'D')
    >>> pprint(g)
    {'A': {'B'},
    'B': {'D', 'A', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'E', 'B'},
    'E': {'D', 'F'},
    'F': {'E', 'C'}}

    >>> g.remove('A')
    >>> pprint(g)
    {'B': {'D', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'E', 'B'},
    'E': {'D', 'F'},
    'F': {'E', 'C'}}

    >>> g.add('G', 'B')
    >>> pprint(g)
    {'B': {'D', 'G', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'E', 'B'},
    'E': {'D', 'F'},
    'F': {'E', 'C'},
    'G': {'B'}}

    >>> g.find_path('G', 'E')
    ['G', 'B', 'D', 'C', 'F', 'E']
    """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def __str__(self):
        # return '{}({})'.format(self.__class__.__name__, dict(self._graph))
        return '{}'.format(self._graph)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove node """
        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Returns True if node1 is connected to node2 """
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (maybe not the shortest)"""
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
