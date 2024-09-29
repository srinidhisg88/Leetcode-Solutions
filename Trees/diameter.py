# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## use post order traversal and add up the heights
        diameter=[0]
        self.getheight(root,diameter)
        return diameter[0]
        
    def getheight(self,root,diameter):
        if not root:
            return 0
        lh=self.getheight(root.left,diameter)
        rh=self.getheight(root.right,diameter)

        diameter[0]=max(lh+rh,diameter[0])
        return 1+max(lh,rh)