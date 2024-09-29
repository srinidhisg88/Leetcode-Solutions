# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## optimal approach is to use post order traversal and check for each node 
        return self.dfsheight(root)!=-1
    def dfsheight(self,root):
        if not root:
            return 0
        left_height=self.dfsheight(root.left)
        if left_height==-1:
            return -1
        right_height=self.dfsheight(root.right)
        if right_height==-1:
            return -1
        if abs(left_height-right_height)>1:
            return -1
        return max(left_height,right_height)+1
            