class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums) // 2

        for n in nums:
            min = nums[0]
            if n < min:
                min = n
        
        return min
            
        