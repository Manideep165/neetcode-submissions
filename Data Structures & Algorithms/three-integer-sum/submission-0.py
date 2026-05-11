class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Final answer list
        res = []

        # Sort array first
        #
        # Why?
        # Helps use two pointers efficiently
        #
        # Example:
        # [-1,0,1,2,-1,-4]
        #
        # becomes:
        # [-4,-1,-1,0,1,2]
        nums.sort()

        # Loop through array
        #
        # i = index
        # a = value at that index
        for i, a in enumerate(nums):

            # Skip duplicates for first number
            #
            # Example:
            # [-1,-1,0,1]
            #
            # If current value equals previous,
            # skip to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointers
            #
            # l = left pointer
            # r = right pointer
            l = i + 1
            r = len(nums) - 1

            # Continue until pointers meet
            while l < r:

                # Current triplet sum
                threeSum = a + nums[l] + nums[r]

                # Sum too large
                #
                # Move right pointer left
                # to reduce sum
                if threeSum > 0:
                    r -= 1

                # Sum too small
                #
                # Move left pointer right
                # to increase sum
                elif threeSum < 0:
                    l += 1

                # Found valid triplet
                else:

                    # Append as LIST
                    #
                    # Your code had:
                    # res.append(a, nums[l], nums[r])
                    #
                    # append accepts ONE argument only
                    res.append([a, nums[l], nums[r]])

                    # Move left pointer
                    l += 1

                    # Skip duplicate second numbers
                    #
                    # Example:
                    # [0,0,0,0]
                    #
                    # Prevent duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        # Return all triplets
        return res
        