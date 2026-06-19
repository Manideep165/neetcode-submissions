class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = maximum money that can be robbed up to house i-2
        # rob2 = maximum money that can be robbed up to house i-1
        rob1, rob2 = 0, 0

        # Iterate through each house
        for n in nums:
            # Decide whether to:
            # 1. Rob current house (n + rob1)
            # 2. Skip current house (rob2)
            temp = max(n + rob1, rob2)

            # Shift the window forward
            rob1 = rob2
            rob2 = temp

        # rob2 stores the maximum amount that can be robbed
        return rob2