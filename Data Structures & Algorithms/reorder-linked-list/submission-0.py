# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        # -----------------------------------
        # STEP 1: Find middle of linked list
        # -----------------------------------

        slow, fast = head, head.next

        # Slow moves 1 step
        # Fast moves 2 steps
        #
        # When fast reaches end,
        # slow reaches middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # -----------------------------------
        # STEP 2: Reverse second half
        # -----------------------------------

        # Start of second half
        second = slow.next

        # Split list into two halves
        slow.next = None

        # Previous node for reversal
        prev = None

        # Reverse linked list
        while second:

            # Save next node
            tmp = second.next

            # Reverse pointer
            second.next = prev

            # Move prev forward
            prev = second

            # Move second forward
            second = tmp

        # -----------------------------------
        # STEP 3: Merge two halves
        # -----------------------------------

        first = head
        second = prev

        # Merge alternately
        while second:

            # Save next nodes
            tmp1 = first.next
            tmp2 = second.next

            # Connect nodes
            first.next = second
            second.next = tmp1

            # Move pointers
            first = tmp1
            second = tmp2
        