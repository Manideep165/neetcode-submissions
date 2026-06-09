class MedianFinder:

    def __init__(self):

        # Max heap for the smaller half of the numbers.
        # Python only provides a min heap, so values are
        # stored as negatives to simulate a max heap.
        self.small = []

        # Min heap for the larger half of the numbers.
        self.large = []

    def addNum(self, num: int) -> None:

        # Add the new number to the max heap.
        heapq.heappush(self.small, -1 * num)

        # Ensure every number in 'small' is less than or
        # equal to every number in 'large'.
        if (
            self.small and self.large and
            (-1 * self.small[0]) > self.large[0]
        ):
            # Move the largest element from small
            # to large.
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance if small has more than one extra element.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance if large has more than one extra element.
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:

        # If small contains one extra element,
        # its top is the median.
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # If large contains one extra element,
        # its top is the median.
        if len(self.large) > len(self.small):
            return self.large[0]

        # If both heaps have equal size,
        # median is the average of their top elements.
        return (
            (-1 * self.small[0] + self.large[0]) / 2
        )