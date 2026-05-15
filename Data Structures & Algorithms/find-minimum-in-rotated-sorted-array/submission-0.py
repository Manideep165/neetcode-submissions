class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        min = 1

        for n in nums:
            if n < min:
                min = n
        
        return min
            
        