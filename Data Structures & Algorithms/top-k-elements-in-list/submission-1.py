class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          # Dictionary to store frequency of each number
        #
        # Example:
        # {
        #   1: 3,
        #   2: 2,
        #   3: 1
        # }
        count = {} 


        # Create buckets
        #
        # Index = frequency
        # Value = list of numbers having that frequency
        #
        # len(nums) + 1 because maximum possible frequency
        # of a number can be len(nums)
        #
        # Example:
        # nums = [1,1,1,2,2,3]
        #
        # freq =
        # [
        #   [],   -> frequency 0
        #   [],   -> frequency 1
        #   [],   -> frequency 2
        #   [],   -> frequency 3
        #   [],
        #   [],
        #   []
        # ]
        freq = [[] for i in range(len(nums) + 1)]


        # Count frequency of each number

        for n in nums:

             # count.get(n, 0)
            #
            # If n exists in dictionary:
            # return its value
            #
            # Otherwise:
            # return 0
            #
            # Example:
            # first time seeing 1:
            # count.get(1,0) = 0
            #
            # count[1] = 1 + 0 = 1
            #
            # next time:
            # count.get(1,0) = 1
            #
            # count[1] = 1 + 1 = 2
            count[n] = 1 + count.get(n, 0)

            # Put numbers into buckets based on frequency
        #
        # count.items() gives:
        # (number, frequency)
        #
        # Example:
        # (1,3)
        # (2,2)
        # (3,1)
        for n, c in count.items():

            # c = frequency
            #
            # Put number n inside bucket c
            #
            # Example:
            # freq[3].append(1)
            #
            # means:
            # number 1 appears 3 times
            freq[c].append(n)

        res = []    # Result list

        # Traverse buckets backwards
        #
        # Start from highest frequency
        #
        # Example:
        # 6 -> 5 -> 4 -> 3 -> 2 -> 1
        #
        # range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1):

             # freq[i] contains numbers with frequency i
            #
            # Example:
            # freq[3] = [1]
            for n in freq[i]:
                # Add number to result
                res.append(n)

                # Once we collected k elements,
                # return answer immediately
                if len(res) == k:
                    return res 