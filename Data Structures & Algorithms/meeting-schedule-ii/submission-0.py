"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Extract and sort all start times
        start = sorted([i.start for i in intervals])

        # Extract and sort all end times
        end = sorted([i.end for i in intervals])

        # res = maximum rooms needed at any point
        # count = current rooms being used
        res, count = 0, 0

        # Pointers for start and end arrays
        s, e = 0, 0

        # Process all meeting start times
        while s < len(intervals):

            # A meeting starts before the earliest meeting ends
            # Need a new room
            if start[s] < end[e]:
                s += 1
                count += 1

            # A meeting has ended before (or exactly when)
            # the next meeting starts, so reuse a room
            else:
                e += 1
                count -= 1

            # Track the maximum number of rooms used
            res = max(res, count)

        return res