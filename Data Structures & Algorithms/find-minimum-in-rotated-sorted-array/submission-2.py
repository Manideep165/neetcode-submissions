class Solution:

    def findMin(self, nums: List[int]) -> int:

        # Store minimum value found
        #
        # Start with first element
        res = nums[0]

        # Left and right pointers
        l, r = 0, len(nums) - 1

        # Binary search
        while l <= r:

            # If current portion is already sorted:
            #
            # Example:
            # [3,4,5]
            #
            # then leftmost element is minimum
            if nums[l] < nums[r]:

                # Update result
                res = min(res, nums[l])

                # No need to continue searching
                break

            # Middle index
            m = (l + r) // 2

            # Update minimum using middle element
            res = min(res, nums[m])

            # Check which side is sorted
            #
            # Example:
            # [4,5,6,7,0,1,2]
            #
            # if nums[m] >= nums[l]
            #
            # left side is sorted
            if nums[m] >= nums[l]:

                # Minimum must be
                # in right half
                l = m + 1

            else:

                # Right side sorted
                #
                # Minimum is in left half
                r = m - 1

        # Return minimum element
        return res
        