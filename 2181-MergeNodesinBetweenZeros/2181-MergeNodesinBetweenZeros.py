
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        # Itterates untill the 2nd last node
        while node.next.next:
            if node.val == 0:
                # Sums all values untill the next zero is seen
                while node.next.val != 0:
                    # Overrides the first zero
                    node.val += node.next.val
                    # Deletes the node it just added to the last one
                    node.next = node.next.next
            else:
                print(123123)
                node = node.next

        # Removes the last node, which is always a zero
        node.next = None


        return head
