# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node.next != None:
            d = math.gcd(node.val,node.next.val)
            temp = node.next
            newNode = ListNode(d,temp)
            node.next = newNode

            node = node.next.next
        
        return head