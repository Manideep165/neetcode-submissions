# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node helps simplify logic
        #
        # Final merged list starts at:
        # dummy.next
        dummy = ListNode()

        # Tail points to end of merged list
        tail = dummy

        # Continue while both lists exist
        while list1 and list2:

            # Compare node values
            if list1.val < list2.val:

                # Attach smaller node
                tail.next = list1

                # Move list1 forward
                list1 = list1.next

            else:

                # Attach smaller node
                tail.next = list2

                # Move list2 forward
                list2 = list2.next

            # Move tail forward
            tail = tail.next

        # One list may still contain nodes
        #
        # Attach remaining nodes directly
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Return merged list
        #
        # Skip dummy node
        return dummy.next