# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ## preorder traversal
        maxsum=[float('-inf')]
        self.getsum(root,maxsum)
        return maxsum[0]
    def getsum(self,root,maxsum):
        if  root is None:
            return 0
        ls=max(0,self.getsum(root.left,maxsum))
        rs=max(0,self.getsum(root.right,maxsum))
        maxsum[0]=max(ls+rs+root.val,maxsum[0])
        return max(ls,rs)+root.val