# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first=head
        second=head
        mark=head
        for _ in range(1,k):
            first=first.next
        mark=first
        while first.next!=None:
            second=second.next
            first=first.next
        mark.val,second.val=second.val,mark.val
        return head