 def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head

        while n > 0:
            second = second.next
            n -= 1
        
        if not second:
            return first.next
        
        while second.next:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return head