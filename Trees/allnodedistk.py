# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph={}
        self.buildGraph(root,None,graph)
        dist=0
        queue=deque([(target,dist)])
        visited=deque(set([target]))
        res=[]
        while queue:
            node,dist=queue.popleft()
            if dist==k:
                res.append(node.val)
            if dist>k:
                break
            
            for n in graph[node]:
                if n not in visited:
                    visited.append(n)
                    queue.append((n,dist+1))
            
        return res


    def buildGraph(self,node:TreeNode,parent:TreeNode,graph):
        if not node:
            return 
        if node not in graph:
            graph[node]=[]

        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        self.buildGraph(node.left,node,graph)
        self.buildGraph(node.right,node,graph)