# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Merges two linked lists
        def mergeLL(n1,n2):
            # Creates a dummy node to add the new nodes to 
            dummy = ListNode()
            node = dummy

            # Adds the next smallest until one of the linked lists are empty
            while n1 and n2:
                if n1.val < n2.val:
                    node.next = ListNode(n1.val)
                    n1 = n1.next
                    node = node.next
                else:
                    node.next = ListNode(n2.val)
                    n2 = n2.next
                    node = node.next

            # It is very possible that one list will be completed before the other
            # We then handle both the first and second having remaning nodes (At most one of these will have nodes left)
            while n1:
                node.next = ListNode(n1.val)
                n1 = n1.next
                node = node.next

            while n2:
                node.next = ListNode(n2.val)
                n2 = n2.next
                node = node.next

            return dummy.next
        
        # If there are no lists to sort we dont need to return anything
        if len(lists) == 0:
            return 
        
        # Sorts 2 lists at a time until we have 1 list left
        while len(lists) > 1:
            lists.append(mergeLL(lists[0],lists[1]))
            lists.pop(0)
            lists.pop(0)
        
        return lists[0]
