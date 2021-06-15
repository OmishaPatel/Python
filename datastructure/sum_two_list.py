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
    def sum_two_list(self, llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            result = i + j + carry
            print(result)
            if result >=10:
                carry = 1
                remainder = result % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(result)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()




linked_list1 = LinkedList()
linked_list1.append(5)
linked_list1.append(6)
linked_list1.append(3)
linked_list2 = LinkedList()
linked_list2.append(8)
linked_list2.append(4)
linked_list2.append(2)
linked_list1.sum_two_list(linked_list2)