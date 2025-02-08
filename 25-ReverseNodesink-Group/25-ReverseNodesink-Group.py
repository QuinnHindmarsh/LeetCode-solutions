# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(node,k):
            i = 0
            while node and i < k:
                i += 1
                node = node.next
            return node

        dummy = ListNode()
        dummy.next = head 
        prevNode = dummy 

        while True:
            kth = get_kth(prevNode,k)

            if not kth:
                break
            
            nextNode = kth.next

            prev, cur = kth.next, prevNode.next

            while cur != nextNode:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = prevNode.next
            prevNode.next = kth
            prevNode = tmp

        return dummy.next