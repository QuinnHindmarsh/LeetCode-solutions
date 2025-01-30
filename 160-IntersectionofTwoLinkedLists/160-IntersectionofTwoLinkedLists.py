# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        aflag = bflag = False

        while a and b:
            if a == b:
                return a
            
            if a.next == None and not aflag:
                aflag = True
                a = headB
            else:
                a = a.next
            
            if b.next == None and not bflag:
                bflag = True
                b = headA
            else:
                b = b.next

        return None