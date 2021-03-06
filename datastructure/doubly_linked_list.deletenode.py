class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node 

        else:
            new_node = Node(data)
            cur = self.head 
            while cur.next:
                cur = cur.next 
            cur.next = new_node 
            new_node.prev = cur 
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def print_list(self):
        cur = self.head 
        while cur:
            print(cur.data)
            cur = cur.next

    def delete_node(self,key):
        #case 1 where key is head of the list
        cur = self.head
        while cur:
            #case 1 where key is head of the list
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                 # case 2 where key is second node
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    nxt = self.head
                    return
            elif cur.data == key:
                #case 3 where key.next is not pointing to null
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    #case 4 where key.next is null
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete_node(1)
dllist.delete_node(6)
dllist.delete_node(4)

dllist.delete_node(3)
dllist.print_list()        
