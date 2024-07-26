# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# optimized solution to find intersection of nodes
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        t1=headA## assign two dummy nodes
        t2=headB
        while t1!=t2:
            t1=headB if t1==None else t1.next
            t2=headA if t2==None else t2.next
        return t1
        