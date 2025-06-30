# Last updated: 30/06/2025, 17:53:31
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        second = self.split(head)

        sorted_first = self.sortList(head)
        sorted_second = self.sortList(second)

        return self.merged(sorted_first, sorted_second)

    def split(self, head):
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = slow.next
        slow.next = None

        return new_head
        

    def merged(self, l1, l2):
        tail = new = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = ListNode(val=l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(val=l2.val)
                l2 = l2.next
            tail = tail.next

        while l1:
            tail.next = ListNode(val=l1.val)
            l1 = l1.next
            tail = tail.next

        while l2:
            tail.next = ListNode(val=l2.val)
            l2 = l2.next
            tail = tail.next

        return new.next