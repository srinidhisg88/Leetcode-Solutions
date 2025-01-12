"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue=[]
        res=[]
        ## here we are using right to left bfs approach 
        ## assign each rightnode initially to the null 
        ## and update it to the current value
        if not root:
            return None
        
        queue.append(root)
        while queue:
            rightNode=None
            for i in range(len(queue)):
                cur=queue.pop(0)
                cur.next=rightNode
                rightNode=cur
                if cur.right:
                    queue.append(cur.right)
                    queue.append(cur.left)
        return root