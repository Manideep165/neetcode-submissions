class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # l -> buying day
        # r -> selling day
        #
        # Start with:
        # buy on day 0
        # sell on day 1
        l, r = 0, 1

        # Stores maximum profit found
        maxP = 0

        # Continue until r reaches end
        while r < len(prices):

            # If selling price is higher,
            # profit is possible
            if prices[l] < prices[r]:

                # Profit =
                # sell price - buy price
                profit = prices[r] - prices[l]

                # Update maximum profit
                maxP = max(maxP, profit)

            else:

                # Found smaller buying price
                #
                # Move left pointer
                # to current day
                l = r

            # Move selling pointer forward
            r += 1

        # Return maximum profit found
        return maxP