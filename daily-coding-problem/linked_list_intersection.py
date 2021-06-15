class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        found = set()
        currA = headA
        currB = headB
        while currA:
            found.add(currA)
            currA = currA.next
        while currB:
            if currB in found:
                return currB
            currB = currB.next