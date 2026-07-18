class Solution:
    def reverseBits(self, n: int) -> int:
        # Stores the reversed 32-bit number
        res = 0

        # Process all 32 bits
        for i in range(32):

            # Extract the i-th bit from n
            bit = (n >> i) & 1

            # Place it in the mirrored position
            res = res | (bit << (31 - i))

        return res