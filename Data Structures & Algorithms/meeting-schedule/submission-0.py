"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort meetings by start time
        intervals.sort(key=lambda i: i.start)

        # Compare each meeting with the previous one
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            # Overlap exists
            if i1.end > i2.start:
                return False

        # No overlaps found
        return True