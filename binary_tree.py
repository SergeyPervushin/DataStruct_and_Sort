from typing import List


class Tree_node:
    """ Base class for create binary tree root"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)  # закомментировать этот метод после отладки кода(или удалить)!!!


class Binary_tree(Tree_node):
    """ Base binary tree class"""

    def insert(self, data):
        root = self
        query = [root]  # очередь для хранения узлов дерева
        while query:
            current = query.pop(0)
            if current.left is None:
                current.left = data
                return
            else:
                query.append(current.left)

            if current.right is None:
                current.right = data
                return
            else:
                query.append(current.right)

    @staticmethod
    def create_from_list(array: List):
        """
        Build simply binary tree from list as like in Leetcode tasks
        first element of array is root, returns TreeNode(list[0])
        """
        if len(array) == 0:
            return f'There is no data for build binary tree'

        out_tree = Binary_tree(array[0])
        for item in array[1:]:
            item = Tree_node(item)
            out_tree.insert(item)

        return out_tree

    @staticmethod
    def depth(root) -> int:
        if not root:
            return 0
        l_depth = Binary_tree.depth(root.left)
        r_depth = Binary_tree.depth(root.right)
        return max(l_depth, r_depth) + 1    # нужна максимальная глубина (плюс корень)

    @staticmethod
    def convert_to_list(root) -> List:
        """ Convert back to list for checking before pushing to Leetcode"""
        out = [root]
        if root.left is None and root.right is None:
            return out
        steps = Binary_tree.depth(root)
        for i in range(steps):
            if out[i] is not None:
                out.append(out[i].left)
                out.append(out[i].right)
            else:
                continue
        return out


class BST(Tree_node):
    """ Binary search tree class"""

    @staticmethod
    def make_instance(data):
        if not isinstance(data, Tree_node):
            return Tree_node(data)

    @staticmethod
    def insert(root: Tree_node, new_node: Tree_node):

        if root is not None:
            if new_node.val < root.val:
                if root.left is not None:
                    BST.insert(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right is not None:
                    BST.insert(root.right, new_node)
                else:
                    root.right = new_node
        else:
            root = new_node

    @staticmethod
    def list_to_BST(array):
        out = BST(array[0])
        for item in array[1:]:
            BST.insert(out, BST(item))
        return out

    @staticmethod
    def pre_order(root):
        if root:
            print(root.val)
            BST.pre_order(root.left)
            BST.pre_order(root.right)

    @staticmethod
    def post_order(root):
        if root:
            BST.post_order(root.left)
            BST.post_order(root.right)
            print(root.val)

    @staticmethod
    def in_order(root):
        if root:
            BST.in_order(root.left)
            print(root.val)
            BST.in_order(root.right)

    @staticmethod
    def breadth_first_order(root):
        pass


'''Hand test for BST class'''
nums = [7,4,3,None,None,6,19]
# tree = BST.list_to_BST(nums)

x = Binary_tree(10)
y = Binary_tree.create_from_list(nums)


