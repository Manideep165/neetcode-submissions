# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        # Edge case:
        # empty input
        if not lists or len(lists) == 0:
            return None

        # Continue until only one list remains
        while len(lists) > 1:

            # Stores merged pairs
            mergedLists = []

            # Process lists two at a time
            #
            # Example:
            # [l1,l2,l3,l4]
            #
            # merges:
            # (l1,l2)
            # (l3,l4)
            for i in range(0, len(lists), 2):

                # First list
                l1 = lists[i]

                # Second list
                #
                # If odd number of lists,
                # l2 becomes None
                l2 = (
                    lists[i + 1]
                    if (i + 1) < len(lists)
                    else None
                )

                # Merge pair and store result
                mergedLists.append(
                    self.mergeList(l1, l2)
                )

            # Replace old lists with merged lists
            lists = mergedLists

        # Only one fully merged list remains
        return lists[0]

    # Merge two sorted linked lists
    def mergeList(self, l1, l2):

        # Dummy node simplifies merging
        dummy = ListNode()

        # Tail points to end of merged list
        tail = dummy

        # Merge while both lists exist
        while l1 and l2:

            # Choose smaller node
            if l1.val < l2.val:

                tail.next = l1
                l1 = l1.next

            else:

                tail.next = l2
                l2 = l2.next

            # Move tail forward
            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        # Return merged list
        return dummy.next