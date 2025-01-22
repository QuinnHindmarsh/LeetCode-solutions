# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        # Itterates fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast is null we need to delete the head
        if not fast:
            return head.next

        # When fast is null slow points to the n-1th last element
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Deletes the nth element
        slow.next = slow.next.next

        return head