class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] = length of the longest increasing subsequence
        # starting from index i
        LIS = [1] * len(nums)

        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):

            # Compare nums[i] with every element to its right
            for j in range(i + 1, len(nums)):

                # If nums[i] can be followed by nums[j]
                if nums[i] < nums[j]:

                    # Either keep the current LIS length
                    # or extend it using the subsequence at j
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # The answer is the largest LIS starting from any index
        return max(LIS)