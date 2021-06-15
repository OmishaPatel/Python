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

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node deosnt exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return 
        prev_node.next = cur_node.next
        cur_node = None

    def del_node_at_position(self,position):
        cur_node = self.head
        if position == 0:
            cur_node = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 0
        while cur_node and count != position:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None
    
    def node_length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    def node_length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.node_length_recursive(node.next)

    def node_swap(self, key1,key2):
        if key1 == key2:
            return

        prev_node1 = None
        cur_node1 = self.head

        while cur_node1 and cur_node1.data != key1:
            prev_node1 = cur_node1
            cur_node1 = cur_node1.next
        
        prev_node2 = None
        cur_node2 = self.head

        while cur_node2 and cur_node2.data!= key2:
            prev_node2 = cur_node2
            cur_node2 = cur_node2.next

        if not cur_node1 or not cur_node2:
            return
        
        if prev_node1:
            prev_node1.next = cur_node2
        else:
            self.head = cur_node2

        if prev_node2:
            prev_node2.next = cur_node1
        else:
            self.head = cur_node1

        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next
    
    def node_swap_alt(self,key1, key2):
        if key1 == key2:
            return
        x,y = None, None

        cur_node = self.head
        while cur_node:
            if cur_node.data == key1:
                x = cur_node # key1 found
            if cur_node.data == key2:
                y = cur_node # key2 found
            cur_node = cur_node.next
        if x and y:
            x.data, y.data = y.data,x.data
        else:
            return
        
    def remove_duplicates(self):
        prev_node = None
        cur_node = self.head
        dup_values = dict()
        while cur_node:
            if cur_node.data in dup_values:
                prev_node.next = cur_node.next
                cur_node =  None
            else:
                dup_values[cur_node.data] = 1
                prev_node = cur_node
            cur_node = prev_node.next
    def nth_from_lastnode(self, n):
        total_lenght = self.node_length()
        
        cur_node = self.head
        while cur_node:
            if total_lenght == n:
                print(cur_node.data)
                return cur_node
            total_lenght -= 1
            cur_node = cur_node.next
        if cur_node is None:
            return

    def count_occurrences(self,data):
        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                count+=1
            cur_node = cur_node.next
        return count
    def count_occurrences_recursive(self,node,data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)
    def rotate(self,key):
        p = self.head
        q = self.head
        prev_node = None
        count = self.head.data - 1
        while p and count < key:
            prev_node = p
            p = p.next
            count +=1
        p = prev_node
        while q :
            prev_node = q
            q = q.next
        q = prev_node
        q.next = self.head
        self.head = p.next
        p.next = None


linked_list = LinkedList()
linked_list.append(11)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)
linked_list.append(15)
linked_list.append(16)
linked_list.print_list()
linked_list.rotate(14)
linked_list.print_list()
