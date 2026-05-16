# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev points to previous node
        #
        # Initially None because
        # reversed list ends with None
        prev = None

        # curr points to current node
        curr = head

        # Traverse linked list
        while curr:

            # Save next node
            #
            # Important because we are about
            # to change curr.next
            nxt = curr.next

            # Reverse pointer
            #
            # Original:
            # curr -> next
            #
            # After:
            # curr -> prev
            curr.next = prev

            # Move prev forward
            prev = curr

            # Move curr forward
            curr = nxt

        # prev becomes new head
        return prev   