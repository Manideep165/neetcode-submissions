class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Start with n since indices only go from 0 to n-1
        res = len(nums)

        # Add each index and subtract the corresponding value
        # All matching numbers cancel out, leaving the missing number
        for i in range(len(nums)):
            res += (i - nums[i])

        return res