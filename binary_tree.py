
class Tree_node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.leftChild or self.rightChild)

    def has_any_children(self):
        return self.rightChild or self.leftChild

    def hes_both_children(self):
        return self.leftChild and self.rightChild

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.has_left_child():   # for delete function
            self.leftChild.parent = self
        if self.has_right_child():   # for delete function too
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = Tree_node(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = Tree_node(key, val, parent=current_node)
