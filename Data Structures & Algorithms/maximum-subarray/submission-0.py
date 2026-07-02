class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Stores the maximum subarray sum found so far
        maxSub = nums[0]

        # Running sum of the current subarray
        curSum = 0

        # Iterate through each number
        for n in nums:

            # If the running sum becomes negative,
            # it can only hurt future subarrays
            if curSum < 0:
                curSum = 0

            # Extend the current subarray
            curSum += n

            # Update the best answer found so far
            maxSub = max(maxSub, curSum)

        # Return the maximum subarray sum
        return maxSub