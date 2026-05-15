class Solution:

    def search(self, nums: List[int], target: int) -> int:

        # Left and right pointers
        l, r = 0, len(nums) - 1

        # Binary search
        while l <= r:

            # Middle index
            mid = (l + r) // 2

            # Target found
            if target == nums[mid]:
                return mid

            # Check if LEFT half is sorted
            #
            # Example:
            # [4,5,6,7,0,1,2]
            #
            # left half:
            # [4,5,6,7]
            if nums[l] <= nums[mid]:

                # Check if target lies OUTSIDE
                # sorted left half
                #
                # If yes:
                # search right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                # Otherwise target lies
                # inside left half
                else:
                    r = mid - 1

            # Otherwise RIGHT half is sorted
            else:

                # Check if target lies OUTSIDE
                # sorted right half
                #
                # If yes:
                # search left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1

                # Otherwise search right half
                else:
                    l = mid + 1

        # Target not found
        return -1