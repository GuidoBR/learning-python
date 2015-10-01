# http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default.
    >>> connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
    ('C', 'D'), ('E', 'F'), ('F', 'C')]
    >>> g = Graph(connections, directed=True)
    >>> pprint(g._graph)
    {'A': {'B'},
    'B': {'D', 'C'},
    'C': {'D'},
    'E': {'F'},
    'F': {'C'}}

    >>> g = Graph(connections)  # undirected
    >>> pprint(g._graph)
    {'A': {'B'},
    'B': {'D', 'A', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'B'},
    'E': {'F'},
    'F': {'E', 'C'}}

    >>> g.add('E', 'D')
    >>> pprint(g._graph)
    {'A': {'B'},
    'B': {'D', 'A', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'E', 'B'},
    'E': {'D', 'F'},
    'F': {'E', 'C'}}

    >>> g.remove('A')
    >>> pprint(g._graph)
    {'B': {'D', 'C'},
    'C': {'D', 'F', 'B'},
    'D': {'C', 'E', 'B'},
    'E': {'D', 'F'},
    'F': {'E', 'C'}}

    >>> g.add('G', 'B')
    >>> pprint(g._graph)
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

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
