class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Stores all valid combinations whose sum equals target.
        res = []

        def dfs(i, cur, total):

            # If the current sum equals the target,
            # store a copy of the current combination.
            if total == target:
                res.append(cur.copy())
                return

            # Stop if:
            # 1. We've gone past the last number, or
            # 2. The current sum already exceeds the target.
            if i >= len(nums) or total > target:
                return

            # Include nums[i] in the current combination.
            cur.append(nums[i])

            # Since numbers can be reused,
            # stay at the same index.
            dfs(i, cur, total + nums[i])

            # Backtrack: remove the last added number.
            cur.pop()

            # Exclude nums[i] and move to the next number.
            dfs(i + 1, cur, total)

        # Start DFS from index 0,
        # with an empty combination and sum 0.
        dfs(0, [], 0)

        # Return all valid combinations.
        return res