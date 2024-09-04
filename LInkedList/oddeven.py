# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddhead=ListNode(val=-1)
        oddtail=ListNode()
        oddtail=oddhead
        evenhead=ListNode(val=-1)
        eventail=evenhead
        cur=ListNode()
        cur=head
        i=1
        while cur!=None:
            temp=cur
            cur=cur.next
            temp.next=None
            if i%2!=0:## node is odd
                oddtail.next=temp
                
                oddtail=temp
            else:
                eventail.next=temp
                eventail=temp
            i+=1
       
        oddtail.next=evenhead.next
            
        return oddhead.next
    


    

        
        
        