class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Start with the last index as the goal
        goal = len(nums) - 1

        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):

            # If we can jump from index i to the current goal
            # (or beyond it), then index i becomes the new goal
            if i + nums[i] >= goal:
                goal = i

        # If we managed to move the goal back to index 0,
        # then the last index is reachable
        return True if goal == 0 else False