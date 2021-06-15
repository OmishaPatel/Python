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
    def second_largest(self, start, count):
        if start is None:
            return
        if start and count[0] <= 2:
            self.second_largest(start.right, count)
            count[0] += 1

            if count[0] == 2:
                print("2nd largest element is "+str( start.value))
                return
            self.second_largest(start.left, count)
   

        

tree = BinaryTree()
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(10)
tree.insert(12)
print(tree.second_largest(tree.root, [0]))
