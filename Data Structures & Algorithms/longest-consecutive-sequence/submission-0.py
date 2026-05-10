class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list into set
        #
        # Why?
        #
        # Sets provide O(1) lookup time.
        #
        # Example:
        # nums = [100,4,200,1,3,2]
        #
        # numSet =
        # {100,4,200,1,3,2}
        numSet = set(nums)

        # Stores longest consecutive sequence length found
        longest = 0

        # Loop through every number
        for n in nums:
            # Check if current number is
            # START of a sequence
            #
            # Example:
            # n = 1
            #
            # Is 0 in set?
            # NO
            #
            # So 1 is start of sequence.
            #
            # Example:
            # n = 3
            #
            # Is 2 in set?
            # YES
            #
            # So 3 is NOT start.
            #
            # This avoids recomputing sequences.
            if (n - 1) not in numSet:
                # Current sequence length
                length = 0

                # Keep checking consecutive numbers
                #
                # Example:
                # 1,2,3,4
                #
                # while:
                # 1 in set
                # 2 in set
                # 3 in set
                # 4 in set
                while(n + length) in numSet:
                    # Increase sequence length
                    length += 1

                # Update longest sequence found
                #
                # max(a,b) returns larger value
                longest = max(length, longest)

        # Return final answer
        return longest
