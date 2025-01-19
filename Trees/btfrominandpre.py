# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inmap={val:idx for idx,val in enumerate(inorder)}
        def helper(inmap,preorder,prestart,preend,inorder,instart,inend):
            if prestart>preend or instart>inend:
                return
            
            root=TreeNode(preorder[prestart])
            inroot=inmap[root.val]
            numsleft=inroot-instart

            root.left=helper(inmap,preorder,prestart+1,preend+numsleft,inorder,instart,inroot-1)

            root.right=helper(inmap,preorder,prestart+numsleft+1,preend,inorder,inroot+1,inend)
            return root
            
        return helper(inmap,preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

        