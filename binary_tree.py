


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# this is a binary tree, not a binary search tree
class Tree:
    def __init__(self,root):
        self.root = None

    def get_root(self):
        return self.root

    def add(self,value):
        if self.root is not None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    # recursive add
    def _add(self,value,node)
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(value,node.left)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self._add(value,node.right)

    def find(self,value):
        if self.root.value==value:
            return 
