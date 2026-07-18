class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to keep numbers within 32 bits
        mask = 0xFFFFFFFF
        # Maximum positive 32-bit integer
        MAX = 0x7FFFFFFF

        while b != 0:
            # Carry bits
            temp = (a & b) << 1

            # Sum without carry
            a = (a ^ b) & mask

            # Update carry
            b = temp & mask

        # Convert from unsigned 32-bit to signed integer
        return a if a <= MAX else ~(a ^ mask)