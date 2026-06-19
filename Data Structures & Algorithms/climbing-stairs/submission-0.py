class Solution:
    def climbStairs(self, n: int) -> int:
        # 'one' represents the number of ways to reach the current step
        # 'two' represents the number of ways to reach the previous step
        one, two = 1, 1

        # Iterate n - 1 times to build up the Fibonacci sequence
        for i in range(n - 1):
            # Store the current value of 'one' before updating it
            temp = one

            # Number of ways to reach the next step:
            # current ways + previous ways
            one = one + two

            # Move 'two' forward to the old value of 'one'
            two = temp

        # Return the number of ways to reach step n
        return one