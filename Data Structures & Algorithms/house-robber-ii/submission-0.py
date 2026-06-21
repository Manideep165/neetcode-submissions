class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only one house, rob it
        if len(nums) == 1:
            return nums[0]

        # Since the first and last houses are adjacent,
        # we cannot rob both.
        #
        # Consider three cases:
        # 1. Rob only the first house
        # 2. Exclude the first house and solve the rest
        # 3. Exclude the last house and solve the rest
        return max(
            nums[0],
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, nums):
        # rob1 = max money up to house i-2
        # rob2 = max money up to house i-1
        rob1, rob2 = 0, 0

        # Standard House Robber DP
        for n in nums:
            # Choose between:
            # 1. Robbing current house
            # 2. Skipping current house
            newRob = max(rob1 + n, rob2)

            # Move the window forward
            rob1 = rob2
            rob2 = newRob

        # Maximum money that can be robbed
        return rob2
        