# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## using level order traversing and assign index
        if not root:
            return 0

        queue=deque([(root,0)])
        ans=0
        fist,last=None,None
        while queue:
            size=len(queue)
            mmin=queue[0][1]
            for i in range(size):
                cur_id=queue[0][1]-mmin
                node=queue.popleft()

                if i==0:
                    first=cur_id
                if i==size-1:
                    last=cur_id
                if node[0].left:
                    queue.append((node[0].left,2*cur_id+1))
                if node[0].right:
                    queue.append((node[0].right,2*cur_id+2))
            ans=max(ans,last-first+1)
        return ans
        