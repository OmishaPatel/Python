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

    def inorder_traversal(self,start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal =  self.inorder_traversal(start.right, traversal)
        return traversal
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")

        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_traversal(tree.root)
        else:
            print("Traversal tye" +str(traversal_type) + " is not suppoorted")
            return False
    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    def _find(self,value, cur_node):
        if value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._find(value, cur_node.right)
        if cur_node.value == value:
            return True
    def min_node(self, cur_node):
        current = cur_node
        while cur_node.left:
            current = cur_node.left
        return current
    def delete_node(self, value, cur_node):
        if cur_node is None:
            return None
        # eliminate half of possibilities
        if value < cur_node.value:
            cur_node.left = self.delete_node(value, cur_node.left)
        elif value > cur_node.value:
            cur_node.right = self.delete_node(value, cur_node.right)

        else:
            #no child
            if (not cur_node.left) and (not cur_node.right):
                return None
            # One chile
            elif (cur_node.left) and (not cur_node.right):
                cur_node = cur_node.left
            elif (cur_node.right) and (not cur_node.left):
                cur_node = cur_node.right
            #two children
            else:
                min_value = self.min_node(cur_node.right)
                cur_node.value = min_value
                cur_node.right = self.delete_node(min_value, cur_node.right)
        return cur_node
        


tree = BinaryTree()
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(10)
tree.insert(12)
print(tree.find(8))
tree.delete_node(8, tree.root)
print(tree.print_tree("inorder"))

        








