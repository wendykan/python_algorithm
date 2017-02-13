

from collections import deque
import unittest


class Graph:
    class Node:
        def __init__(self,key):
            self.id = key
            self.connected_to = {}

        def add_neighbor(self, neighbor_key, weight):
            self.connected_to[neighbor_key] = weight

        def __str__(self):
            return str(self.id) + 'connected to: ' + str(self.connected_to)

        def get_neighbors(self):
            return self.connected_to.keys()

        def get_id(self):
            return self.id

        def get_connection_weight(self, neighbor_key):
            return self.connected_to[neighbor_key]

    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def add_node(self, node_key):
        node = self.Node(node_key)
        self.nodes[node_key] = node
        self.num_nodes += 1

    def get_node(self, node_key):
        if node_key in self.nodes.keys():
            return self.nodes[node_key]
        else:
            return None

    def get_all_nodes(self):
        return self.nodes.keys()

    def add_edge(self, node1_key, node2_key, weight):
        self.nodes[node1_key].add_neighbor(node2_key, weight)
        self.nodes[node2_key].add_neighbor(node1_key, weight)

    def get_edge_weight(self, node1_key, node2_key):
        if node1_key in self.nodes.keys() and node2_key in self.nodes[node1_key].connected_to.keys():
            return self.nodes[node1_key].connected_to[node2_key]
        else:
            return None

    def bfs(self, start_node, dest_node):
        current_node = start_node
        nodes_to_visit = deque(self.nodes[start_node].get_neighbors())
        visited = set()

        while len(nodes_to_visit)>0: # to_visit list is not empty
            current_node = nodes_to_visit.popleft()
            if current_node==dest_node:
                return True
            if current_node not in visited: # new node
                visited.add(current_node)
                for node in self.nodes[current_node].get_neighbors():
                    nodes_to_visit.append(node)

        return False


class TestGraph(unittest.TestCase):

    def test_bfs_true(self):
        g = Graph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1,2,1)
        g.add_edge(1,3,2)

        self.assertTrue(g.bfs(2,3))

    def test_bfs_false(self):
        g = Graph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1,2,1)
        g.add_edge(1,3,2)

        self.assertFalse(g.bfs(1,4))



if __name__ == '__main__':
    unittest.main()
