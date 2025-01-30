# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        que = deque([root])
        while que:
            node = que.popleft()
            if not node:
                res.append('None')
                continue
            else:
                res.append(str(node.val))
            que.append(node.left)
            que.append(node.right)

        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        data_que = deque(data.split(','))
        root = TreeNode(data_que.popleft())
        node_que = deque([root])
        while data_que:
            node = node_que.popleft()
            val = data_que.popleft()
            if val != 'None':
                node.left = TreeNode(val)
                node_que.append(node.left)
            val = data_que.popleft()
            if val != 'None':
                node.right = TreeNode(val)
                node_que.append(node.right)
    
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))