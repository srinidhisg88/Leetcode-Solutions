# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## bfs traversal with nested hashmap
        hashmap=defaultdict(lambda: defaultdict(lambda:list()))
        queue=deque([(root,(0,0))])
        while queue:
            temp, (x,y)=queue.popleft()
            hashmap[x][y].append(temp.val)
            if temp.left:
                queue.append((temp.left,(x-1,y+1)))
            if temp.right:
                queue.append((temp.right,(x+1,y+1)))
        ans=[]

        for x in sorted(hashmap.keys()):
            col=[]
            for y in sorted(hashmap[x].keys()):
                col.extend(sorted(hashmap[x][y]))
            ans.append(col)
        return ans
