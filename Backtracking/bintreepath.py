# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        dep=[]
        
        def backtrack(root):
            if not root:
                return

            dep.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(dep))
            else:
            
                backtrack(root.left)
            
                backtrack(root.right)
            dep.pop()
        backtrack(root)
        return res
        