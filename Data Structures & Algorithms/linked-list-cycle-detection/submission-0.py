# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Two pointers
        #
        # slow moves 1 step
        # fast moves 2 steps
        slow = head
        fast = head

        # Continue while fast pointer
        # can still move ahead
        #
        # fast and fast.next required
        # to safely do fast.next.next
        while fast and fast.next:

            # Move slow pointer by 1
            slow = slow.next

            # Move fast pointer by 2
            fast = fast.next.next

            # If pointers meet,
            # cycle exists
            #
            # Why?
            #
            # Fast pointer eventually catches
            # slow pointer inside cycle
            if slow == fast:
                return True

        # If fast reaches end,
        # no cycle exists
        return False