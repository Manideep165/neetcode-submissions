class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time
        intervals.sort(key=lambda i: i[0])

        # Start the output with the first interval
        output = [intervals[0]]

        # Process the remaining intervals
        for start, end in intervals[1:]:

            # End value of the last merged interval
            lastEnd = output[-1][1]

            # If intervals overlap, merge them
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            # Otherwise, add a new interval
            else:
                output.append([start, end])

        # Return merged intervals
        return output