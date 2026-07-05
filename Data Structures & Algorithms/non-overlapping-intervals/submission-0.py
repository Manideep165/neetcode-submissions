class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time
        intervals.sort()

        # Number of intervals removed
        res = 0

        # End of the previously kept interval
        prevEnd = intervals[0][1]

        # Process remaining intervals
        for start, end in intervals[1:]:

            # No overlap
            if start >= prevEnd:
                prevEnd = end

            # Overlap detected
            else:
                # Remove one interval
                res += 1

                # Keep the interval with the smaller end time
                # because it leaves more room for future intervals
                prevEnd = min(end, prevEnd)

        # Return number of removed intervals
        return res