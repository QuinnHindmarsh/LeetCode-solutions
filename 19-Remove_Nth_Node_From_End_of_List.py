"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


# Solution one - two pass O(n) time and O(1) space
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        node = head

        # Gets length of the linked list
        while node:
            leng += 1
            node = node.next

        # Linked list only contains 1 element (the head)
        if leng == 1:
            return None

        # The element we want to delte is the head
        if leng == n:
            return head.next

        node = head
        # Itterates untill the node before the one we want to delete
        for i in range((leng - n)-1):
            node = node.next

        # Deletes the node we want to delete
        node.next = node.next.next

        return head


# Solution two - one pass O(n) time and O(1) space
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

# My solution
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/6207262/one-and-two-pass-solution-by-quinnhindma-a0xz/
