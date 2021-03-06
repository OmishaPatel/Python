class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")

        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_traversal(tree.root)
        elif traversal_type == "reverseorder":
            return self.reverse_order_traversal(tree.root)
        else:
            print("Traversal tye" +str(traversal_type) + " is not suppoorted")
            return False



    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal


    def inorder_traversal(self,start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal =  self.inorder_traversal(start.right, traversal)
        return traversal
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.postorder_traversal(start.left, traversal)
        return traversal
    def level_order_traversal(self, start):
        if start:
            queue = Queue()
            queue.enqueue(start)
            traversal = ""
            while len(queue) > 0:
                traversal += str(queue.peek()) + "-"
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return traversal
    def reverse_order_traversal(self, start):
        if start:
            stack = Stack()
            queue = Queue()
            traversal = ""
            queue.enqueue(start)
            while len(queue) > 0:
                node = queue.dequeue()
                stack.push(node)
                
                if node.right:
                    queue.enqueue(node.right)
                if node.left:
                    queue.enqueue(node.left)
            while len(stack) > 0:
                node = stack.pop()
                traversal += str(node.value) + "-"
            return traversal


tree =  BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverseorder"))