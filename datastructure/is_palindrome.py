class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
    def is_palindrome(self):
        # s =""
        # p = self.head
        # while p:
        #     s+= p.data
        #     p = p.next
        # return s == s[::-1]
        #Method 2
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

linked_list = LinkedList()
linked_list1 = LinkedList()
linked_list1.append("A")
linked_list1.append("B")
linked_list1.append("C")
linked_list.append("R")
linked_list.append("A")
linked_list.append("C")
linked_list.append("E")
linked_list.append("C")
linked_list.append("A")
linked_list.append("R")
print(linked_list.is_palindrome())
print(linked_list1.is_palindrome())
