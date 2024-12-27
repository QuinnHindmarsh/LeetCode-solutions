"""
2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

"""

# Solution one - O(n) space, O(1) time


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
                node = node.next

        # Removes the last node, which is always a zero
        node.next = None

        return head

# Solution two - O(n) time and O(1) space still, however runtime is half of the other solution


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        # Iterate over all nodes
        while node:
            # Sums all values untill the next zero is seen
            while node.next.val != 0:
                # Overrides the first zero
                node.val += node.next.val
                # Deletes the node it just added to the last one
                node.next = node.next.next

            # Deltes node.next, which is garunteed to be a zero
            node.next = node.next.next
            # Increments to the next value to merge (or to a null node)
            node = node.next

        return head

# My solution
# https://leetcode.com/problems/merge-nodes-in-between-zeros/solutions/6191492/simple-efficient-on-iterative-solution-b-h83i/
