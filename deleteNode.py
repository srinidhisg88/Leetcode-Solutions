# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Delete a node in the linked list without using a head
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp=node.val
        prev=None
        cur=node
        
        while cur.next!=None:
            prev=cur
            cur=cur.next
            prev.val=cur.val
        cur.val=temp
        prev.next=None
