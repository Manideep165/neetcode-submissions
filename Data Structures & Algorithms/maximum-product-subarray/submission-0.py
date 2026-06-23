class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with the largest single element
        # This handles cases where all numbers are negative
        res = max(nums)

        # curMax = maximum product ending at current position
        # curMin = minimum product ending at current position
        curMin, curMax = 1, 1

        # Iterate through each number
        for n in nums:

            # A zero breaks any subarray product
            if n == 0:
                curMin, curMax = 1, 1
                continue

            # Store current max before updating it
            # because curMin needs the old value
            tmp = curMax * n

            # Calculate new maximum product ending here
            curMax = max(
                n * curMax,
                n * curMin,
                n
            )

            # Calculate new minimum product ending here
            curMin = min(
                tmp,
                n * curMin,
                n
            )

            # Update global maximum product
            res = max(res, curMax)

        # Return the maximum product found
        return res