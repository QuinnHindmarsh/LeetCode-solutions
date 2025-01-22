class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        n1 = ''
        n2 = ''

        while l1:
            n1 += str(l1.val)
            l1 = l1.next

        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        
        
        n1 = n1[::-1]
        n2 = n2[::-1]

        num = str(int(n1) + int(n2))
        
        dummy = ListNode()
        node = dummy

        for i in range(len(num) -1, -1,-1):
            node.next = ListNode(int(num[i]))
            node = node.next

        return dummy.next