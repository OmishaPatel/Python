import math
prev = -math.inf
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value is already present in tree.")
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            print(str(cur_node.value))
            self._inorder_print_tree(cur_node.left)
            self._inorder_print_tree(cur_node.right)
            

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.value
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)


            
        
        


tree = BinaryTree()
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(10)
tree.insert(12)

tree1 = BinaryTree()
tree1.root = Node(8)
tree1.root.left = Node(3)
tree1.root.right = Node(10)
tree1.root.left.left = Node(2)
tree1.root.left.right = Node(25)
print(tree.is_bst_satisfied())
print(tree1.is_bst_satisfied())