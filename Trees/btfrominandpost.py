# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inmap={val:idx for idx,val in enumerate(inorder)}
        def helper(inmap,postorder,poststart,postend,inorder,instart,inend):
            if poststart>postend or instart>inend:
                return
            
            root=TreeNode(postorder[postend])
            inroot=inmap[root.val]
            numsleft=inroot-instart

            root.left=helper(inmap,postorder,poststart,poststart+numsleft-1,inorder,instart,inroot-1)

            root.right=helper(inmap,postorder,poststart+numsleft,postend-1,inorder,inroot+1,inend)
            return root
            
        return helper(inmap,postorder,0,len(postorder)-1,inorder,0,len(inorder)-1)

        