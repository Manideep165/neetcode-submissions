class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create result array filled with 1s
        #
        # Example:
        # nums = [1,2,3,4]
        #
        # res =
        # [1,1,1,1]
        #
        # We will later store:
        # prefix products * postfix products
        res = [1] * (len(nums))

        # Prefix product variable
        #
        # Stores product of all elements
        # to the LEFT of current index

        prefix = 1
        for i in range(len(nums)): # Left-to-right pass
            # Store current prefix product
            #
            # Example:
            # before index 2,
            # product of left side is:
            # nums[0] * nums[1]
            res[i] = prefix 

            # Update prefix by multiplying
            # current number
            #
            # Example:
            # prefix *= nums[i]
            #
            # prefix evolves like:
            # 1 -> 1 -> 2 -> 6 -> 24
            prefix *= nums[i]

        # Postfix product variable
        #
        # Stores product of all elements
        # to the RIGHT of current index
        postfix = 1

        # Right-to-left pass
        #
        # range(start, stop, step)
        #
        # Example for length 4:
        # 3 -> 2 -> 1 -> 0
        for i in range(len(nums) - 1, -1, -1):

            # Multiply existing prefix product
            # with postfix product
            #
            # res[i] currently contains:
            # product of left side
            #
            # postfix contains:
            # product of right side
            #
            # Multiplying them gives:
            # product of all elements
            # except nums[i]

            res[i] *= postfix

            # Update postfix product
            #
            # Example:
            # postfix evolves:
            # 1 -> 4 -> 12 -> 24
            postfix *= nums[i]
        return res 