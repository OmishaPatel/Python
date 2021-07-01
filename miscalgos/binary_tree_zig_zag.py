class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        from collections import deque
        deque = deque()
        deque.append(root)
        counter = 1
        
        while deque:
            size = len(deque)
            lst = []
            for i in range(size):
                
                # if odd, get element from left side
                # save the element's value to list
                # add the element's left and right nodes 
                # to the right side of the deque
                
                if counter % 2 != 0:
                    cur = deque.popleft()
                    lst.append(cur.val)
                    if cur.left:
                        deque.append(cur.left)
                    if cur.right:
                        deque.append(cur.right)
                        
                # if even, get element from right side
                # save the element's value to list
                # add the element's right and left nodes 
                # to the left side of the deque
                
                elif counter % 2 == 0:
                    cur = deque.pop()
                    lst.append(cur.val)
                    if cur.right:
                        deque.appendleft(cur.right)
                    if cur.left:
                        deque.appendleft(cur.left)
            counter += 1
            result.append(lst)
        return result