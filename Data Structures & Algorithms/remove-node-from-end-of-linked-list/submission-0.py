# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        # Dummy node helps handle
        # edge cases easily
        #
        # Example:
        # removing head node
        dummy = ListNode(0, head)

        # Two pointers
        left = dummy
        right = head

        # Move right pointer n steps ahead
        #
        # Creates gap of n nodes
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers together
        #
        # When right reaches end,
        # left will be just BEFORE
        # node to remove
        while right:
            left = left.next
            right = right.next

        # Remove nth node
        #
        # Skip target node
        left.next = left.next.next

        # Return new head
        #
        # dummy.next skips fake node
        return dummy.next