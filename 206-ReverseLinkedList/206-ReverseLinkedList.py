# Last updated: 16/05/2025, 12:12:05
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        prev = None
        cur = head

        while cur: 
            next = cur.next
            cur.next = prev
            
            prev = cur
            cur = next


    

        return prev