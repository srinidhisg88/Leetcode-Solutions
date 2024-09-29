# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        
        res=[]
        if not root:
            return res
        
        res.append(root.val)
        while queue:
            ans=[]
            
            n=len(queue)
            
            for i in range(n):
                node=queue.pop(0)
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(ans)
        return res


        