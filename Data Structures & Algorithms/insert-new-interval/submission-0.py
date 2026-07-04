class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Result list
        res = []

        # Process each interval
        for i in range(len(intervals)):

            # Case 1:
            # New interval comes completely before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)

                # Add remaining intervals and return
                return res + intervals[i:]

            # Case 2:
            # New interval comes completely after current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3:
            # Intervals overlap, merge them
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # merged start
                    max(newInterval[1], intervals[i][1])   # merged end
                ]

        # If we never inserted it, add the merged interval at the end
        res.append(newInterval)

        return res