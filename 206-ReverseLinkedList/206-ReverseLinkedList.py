# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        stack = [] 
        node = head

        while node:
            stack.insert(0,node.val)
            node = node.next

        node = head
        
        while node:
            node.val = stack.pop(0)
            node = node.next

        return head