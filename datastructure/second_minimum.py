class Node(object):
    def __init__(self, value):
        self.value = value
        self.left =  None
        self.right = None


class BinaryTree(object):
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

    def second_minimum(self, start, count):
        if start is None:
            return
        if start and count[0] <=2:
            self.second_minimum(start.left, count)
            count[0] +=1
            if count[0] == 2:
                print("2nd smallest element is "+str( start.value))
            self.second_minimum(start.right, count)
tree = BinaryTree()
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(10)
tree.insert(12)
print(tree.second_minimum(tree.root, [0]))