class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Stores maximum area found
        res = 0

        # Two pointers
        #
        # l -> left pointer
        # r -> right pointer
        l, r = 0, len(heights) - 1

        # Continue until pointers meet
        while l < r:

            #formula to calculate the area between heights
            area = (r - l) * min(heights[l], heights[r])

            #updating the max height found so far at each iteration
            res = max(res, area)

            # Move pointer at smaller height
            #
            # Why?
            #
            # Area depends on minimum height.
            # To possibly increase area,
            # we need a taller line.

            if heights[l] < heights[r]:
                # Move left pointer right
                l += 1
            else:
                # Move right pointer left
                r -= 1
        
        # Return maximum area found
        return res 
        